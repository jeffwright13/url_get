#!/usr/bin/python

def main():
    input_file = 'URLs/40URLs.txt'
    output_file = 'logs/results-Test'
    
    # Get list of URLs from external file and store it in 
    # a dictionary named 'URLs'
    URLs = get_urls(input_file)
    
    # Visit each site in the 'URLs' dictionary, and store the
    # page load times for each in dictionary named 'results'
    results = visit_urls(URLs)
    
    # Write the 'results' dictionary to the file 'output_file'
    write_to_logfile(output_file, results)
    
def get_urls(url_file):
    '''
    Synopsis:
        get_urls(url_file)
    
    Description:
        
    Input Arguments:
        url_file: A comma-separated-variable (CSV) file with
                  column1=URL, column2=website header text
    
    Returns:
        URLs: a dictionary with key = URL of site, 
              val = text to expect in site title
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
    
    for url, title in url_dict.iteritems():
        print ("Loading %s at time %s" % (url, time.strftime('%X')))
        start_time = time.time()
        firefox.get(url)
        end_time = time.time()
        assert title in firefox.title
        print ("Finished loading %s at time %s" % (url, time.strftime('%X')))
        print ("Time to load: %.1f\n" % (end_time - start_time))
        results_dict[url] = end_time - start_time
        
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
    
if __name__ == "__main__":
    main()