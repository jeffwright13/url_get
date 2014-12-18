import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FortyURLsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_navigate_40_URLs(self):
        URLs = {
                    'http://www.fcc.gov': 'FCC',
                    'http://www.cnbc.com': 'CNBC',
                    'http://www.ymca.com': 'the Y',
                    'http://www.walmart.com': 'Walmart',
                    'http://www.lowes.com': "Lowe's",
                    'http://www.ebay.com': 'eBay',
                    'http://www.mcdonalds.com': 'Donald',
                    'http://www.monoprice.com': 'price',
                    'http://www.kodak.com': 'Kodak',
                    'http://my.hughesnet.com': 'Support Center',
                    'http://www.yahoo.com': 'Yahoo',
                    'http://www.verizon.com': 'Verizon',
                    'http://www.autozone.com': 'Auto',
                    'http://www.fiatusa.com': 'FIAT',
                    'http://www.apple.com': 'Apple',
                    'http://www.hp.com': 'HP',
                    'http://www.umuc.edu': 'UMUC',
                    'http://www.bankofamerica.com': 'Bank of America',
                    'http://www.wellsfargo.com': 'Wells Fargo',
                    'http://www.capitalone.com': 'Capital One',
                    'http://www.suntrust.com': 'SunTrust',
                    'http://www.pnc.com': 'PNC Bank',
                    'http://www.ameritrade.com': 'Ameritrade',
                    'http://www.fidelity.com': 'Fidelity',
                    'http://www.gmail.com': 'Gmail',
                    'http://www.yahoomail.com': 'Yahoo',
                    'http://www.facebook.com': 'Facebook',
                    'http://www.trsretire.com': 'Transamerica',
                    'http://www.mafcu.org': 'Mid-Atlantic',
                    'http://www.americanexpress.com': 'American Express',
                    'http://www.nasafcu.com': 'NASA',
                    'http://www.navyfederal.org': 'Navy',
                    'http://www.fairfaxcu.org': 'Fairfax',
                    'http://www.secumd.org': 'SECU MD',
                    'http://www.towerfcu.org': 'Tower',
                    'http://www.nihfcu.org': 'NIH',
                    'http://www.andrewsfcu.org': 'Andrews'
                    }
        driver = self.driver
        for url, title in URLs.iteritems():
            print ("Loading %s..." % url)
            start_time = time.time()
            driver.get(url)
            self.assertIn(title, driver.title)
            end_time = time.time()
            print ("Finished loading %s." % url)
            print ("Time to load: %.1f" % (end_time - start_time))
            time.sleep(.25)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()