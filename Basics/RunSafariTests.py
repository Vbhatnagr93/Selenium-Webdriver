from selenium import webdriver  #import the webdriver from selenium package
import os
import time

class RunSafaritests():
    def test(self):
        serverLocation = "/Users/revelrycomputer/Desktop/workspace_python/seleniumwd2/lib/selenium-server-standalone-2.53.1.jar"
        os.environ["SELENIUM_SERVER_JAR"] = serverLocation #set environment var to server location
        driver = webdriver.Safari()  # create an instance of the webdriver

        driver.get("http://www.letskodeit.com") #open the provided url



safari = RunSafaritests()

safari.test()

time.sleep(100)






