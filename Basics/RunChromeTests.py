from selenium import webdriver  #import the webdriver from selenium package
import os
import time

class RunChromeTests():
    def test(self):
        driverLocation = "/Users/revelrycomputer/Desktop/workspace_python/seleniumwd2/lib"
        os.environ["webdriver.chrome.driver"] = driverLocation #pass the environment var to driverlocation
        driver = webdriver.Chrome()  #  # create an instance of the webdriver

        driver.get("http://www.letskodeit.com") #open the provided url



chrome = RunChromeTests()

chrome.test()

time.sleep(100)






