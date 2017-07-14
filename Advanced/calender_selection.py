from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalenderSelection():

    def test1(self):
        baseurl = "http://www.expedia.com"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        #click flights tab

        driver.find_element_by_id("tab-flight-tab-hp").click()
        #Find Departing field
        departingField = driver.find_element_by_id("flight-departing-hp-flight")
        #Click departing field
        departingField.click()
        #Find the date to be selected
        dateToSelect = driver.find_element(By.XPATH, "//div[@id='flight-departing-wrapper-hp-flight']//button[text()='31']")
        #click the date
        dateToSelect.click()

        time.sleep(3)
        driver.quit()


ff = CalenderSelection()
ff.test1()