#!/usr/bin/python

def main():
    # Internal execution variables
    input_file = 'URLs/4URLs.txt'
    num_iterations = 3
    
    # main execution class instance
    testRun = TestRun()
    
    # Populate dict of URLs to visit from specified external file
    URLs = get_urls(input_file)

    # Run thru each URL and update execution class instance
    # with results
    for iter in range(0, num_iterations):
        print ('Iteration #%s' % (iter+1))
        print ('=============')
        
        # Instantiate a new Iterations() instance for this iteration
        testRun.iterations.append(Iteration())

        # Visit each site in the 'URLs' dictionary, and store the
        # page load times for each in dictionary named 'results'
        results = visit_urls(URLs)
        testRun.iterations[iter] = results
        
        # Write the 'results' dictionary to the file 'output_file'
        filename = 'logs/' + get_filename() + '.csv'
        write_to_logfile(filename, results)
        
    # Run final results thru stats generator
    generate_stats(testRun)
    
def get_urls(url_file):
    '''
    Synopsis:
        get_urls(url_file)
    
    Description:
        Takes an external file, in CSV format, the two
        columns of which are a URL (e.g. 'http://www.cnn.com') 
        and some verification text expected in that site's 
        HTML <title> tag (e.g. 'CNN').
        Stores an internal data struct (dictionary/associative
        array), in the format {URL: title-text}.
        
    Input Arguments:
        url_file: A comma-separated-variable (CSV) file with
                  column1=URL, column2=website header text
    
    Returns:
        URLs: a dictionary with key = URL of site, 
              val = text to expect in site's HTML <title>
    '''

    URLs = {}
    with open(url_file, 'r') as file:
        for line in file:
            (key, val) = line.split(',')
            URLs[key.strip()] = val.strip()
    return URLs

def visit_urls(url_dict):
    '''
    Synopsis:
        visit_urls(url_dict)
    
    Description:
        
    Input Arguments:
        url_dict: A Python dictionary object with key=URL,
        value=website header text
    
    Returns:
        results_dict: a Python dictionary that contains the results
                      of this run; key=url, value=page load time
    '''

    import time    
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    
    results_dict = {}

    # Launch browser using Selenium driver
    firefox = webdriver.Firefox()
    
    # Visit each URL and verify expected title
    for url, title in url_dict.iteritems():
        print ("Loading %s at time %s" % (url, time.strftime('%X')))
        start_time = time.time()
        firefox.get(url)
        end_time = time.time()
        assert title in firefox.title
        print ("Finished loading %s at time %s" % (url, time.strftime('%X')))
        print ("Time to load: %.1f\n" % (end_time - start_time))
        results_dict[url] = end_time - start_time
        
    # Close all browser windows
    for window in firefox.window_handles:
        firefox.switch_to_window(window)
        firefox.close()
    
    return results_dict

def write_to_logfile(log_file, dict):
    '''
    Synopsis:
        write_to_logfile(log_file)
    
    Description:
        
    Input Arguments:
        log_file: Name of a log file to write/create
        dict: dictionary of key,value pairs to write to log_file
    
    Returns:
        None
    '''

    try:
        fh = open(log_file, 'w')
        
        for key, value in dict.iteritems():
            fh.write(key + ',' + str(value) + '\n')
        
        fh.close()
    except IOError:
        print ('Error either opening or writing log file %s' % log_file)
    
def get_filename():
    '''
    Synopsis:
        get_filename()
    
    Description:
        Function to generate a string representation of a filename based
        on the current date and time. Useful for logfile names.
        
    Input Arguments:
        None
    
    Returns:
        String
    '''
    import time
    timestr = time.strftime('%Y%m%d-%H%M%S')
    return timestr

def generate_stats(testRunObj):
    '''
    Synopsis:
        generate_stats(testRunObj)
    
    Description:
        Function to generate statistics of TestRun instance
        
    Input Arguments:
        testRunObj: an instance of type TestRun
    
    Returns:
        None
    '''
    for k in testRunObj.iterations:
        print (k)

class Iteration(object):
    '''
    '''
    def __init__(self):
        self.load_times = {}
        self.average = 0.0
        self.std_dev = 0.0

    def __str__(self):
        print ('load_times:', self.load_times)
        print ('average:   ', self.average)
        print ('std_dev:   ', self.std_dev)
    
class TestRun(object):
    '''
    '''
    def __init__(self):
        self.iterations = []

    def __str__(self):
        print ('iterations:', self.iterations)
    
if __name__ == "__main__":
    main()