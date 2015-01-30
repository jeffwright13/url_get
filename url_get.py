#!/usr/bin/python

def main():
    # Internal execution variables
    input_file = 'URLs/40URLs.txt'
    num_iterations = 5
    browser = 'Firefox' # Valid choices: "Firefox", "Ie"
    
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
        # and append it to the TesRun() instance
        i = Iteration()
        testRun.iterations.append(i)

        # Visit each site in the 'URLs' dictionary, and store the
        # page load times for each in dictionary named 'results'
        results = visit_urls(URLs, browser)
        testRun.iterations[iter].load_times = results
        
        # Write this iteration's results to file
        filename = 'logs/' + get_filename() + '.csv'
        write_to_logfile(filename, results, 'log')
        
    # Run final results thru stats generator
    generate_stats(testRun)
    
    # Write the whoe test run's stats to file
    filename = 'logs/' + get_filename() + '_stats' + '.csv'
    write_to_logfile(filename, testRun.stats.averages, 'stats')
    
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

def visit_urls(url_dict, br):
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
    
    results_dict = {}

    # Launch browser using Selenium driver
    if br == 'Firefox':
        browser = webdriver.Firefox()
    elif br == 'Ie':
        browser = webdriver.Ie()
    else:
        raise ValueError('Browser type not supported.')
    
    # Visit each URL and verify expected title
    for url, title in url_dict.iteritems():
        print ("Started loading %s at time %s" % (url, time.strftime('%X')))
        start_time = time.time()
        browser.get(url)
        end_time = time.time()
        assert title in browser.title
        print ("Finished loading %s at time %s" % (url, time.strftime('%X')))
        print ("Time to load: %.1f\n" % (end_time - start_time))
        results_dict[url] = end_time - start_time
        
    # Close all browser windows
    for window in browser.window_handles:
        browser.switch_to_window(window)
        browser.close()
    
    return results_dict

def write_to_logfile(log_file, dict, type=None):
    '''
    Synopsis:
        write_to_logfile(log_file)
    
    Description:
        
    Input Arguments:
        log_file: Name of a log file to write/create
        dict: dictionary of key,value pairs to write to log_file
        type: type of logfile to write ('log', 'stats')
    
    Returns:
        None
    '''
    import os.path
    
    directory = os.path.dirname(log_file)
    if not os.path.exists(directory):
        os.makedirs(directory)

    if type == 'log':
        header_row = 'URL' + ',' + 'Load Time'
    elif type == 'stats':
        header_row = 'URL' + ',' + 'Avg load Time'
    else:
        raise Exception, 'Invalid type passed to function write_to_logfile()'

    try:
        fh = open(log_file, 'w')
        
        fh.write(header_row + '\n')
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
        Statistics() object
    '''
    import numpy
    
    url_list = testRunObj.iterations[0].load_times.keys()
    N = len(testRunObj.iterations)
    K = len(url_list)
    print "N (# iterations), K (# URLs): ", (N, K)
    
    for url in url_list:
        time_list = []
        for iter in testRunObj.iterations:
            time_list.append(iter.load_times[url])

        testRunObj.stats.averages[url] = numpy.average(time_list)
        testRunObj.stats.variances[url] = numpy.var(time_list)
        testRunObj.stats.std_devs[url] = numpy.std(time_list)
        
    print "Averages: \n", testRunObj.stats.averages
    print "Variances: \n", testRunObj.stats.variances
    print "Std Devs: \n", testRunObj.stats.std_devs

class TestRun(object):
    '''
    '''
    def __init__(self):
        self.iterations = []
        self.stats = Statistics()

class Iteration(object):
    '''
    '''
    def __init__(self):
        self.load_times = {}

class Statistics(object):
    '''
    '''
    def __init__(self):
        self.times     = {}
        self.averages  = {}
        self.variances = {}
        self.std_devs  = {}

if __name__ == '__main__':
    main()

