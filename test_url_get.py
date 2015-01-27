#!/usr/bin/python

import unittest
import url_get

class TestGetURLs(unittest.TestCase):
    '''Unit tests for function get_urls()'''

    def setUp(self):
        pass

    def test_get_urls_correct(self):
        input_file = 'URLs/4URLs.txt'
        correct_result = {'http://www.fcc.gov': 'FCC', 'http://www.cnbc.com': 'CNBC', 'http://www.suntrust.com': 'SunTrust', 'http://www.pnc.com': 'PNC Bank'}
        URLs = url_get.get_urls(input_file)
        self.assertEqual(URLs, correct_result)
        
    def test_get_urls_incorrect(self):
        input_file = 'URLs/4URLs.txt'
        incorrect_result = {'http://www.fcc.gov': 'F', 'http://www.cnbc.com': 'C'}
        URLs = url_get.get_urls(input_file)
        self.assertNotEqual(URLs, incorrect_result)

    def tearDown(self):
        pass        

class TestVisitURLs(unittest.TestCase):
    '''Unit tests for function visit_urls()'''

    def setUp(self):
        pass
        
    def test_visit_urls(self):
        pass

    def tearDown(self):
        pass

class TestWriteToLogfile(unittest.TestCase):
    '''Unit tests for function write_to_logfile()'''

    def setUp(self):
        pass

    def test_write_to_logfile(self):
        pass

    def tearDown(self):
        pass

class TestGetFilename(unittest.TestCase):
    '''Unit tests for function get_filename()'''

    def setUp(self):
        pass

    def test_get_filename(self):
        pass
        
    def tearDown(self):
        pass

class TestGenerateStats(unittest.TestCase):
    '''Unit tests for function generate_stats()'''

    def setUp(self):
        pass

    def test_generate_stats(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
