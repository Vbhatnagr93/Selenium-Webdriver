from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AutoComplete():

    def test1(self):
        baseurl = "http://www.southwest.com"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        # Send Partial Data
        cityField = driver.find_element_by_id("air-city-departure")
        cityField.send_keys("new")
        time.sleep(3)
        #Find the item and click
        itemToSelect = driver.find_element(By.XPATH, ".//div[@id='js-menu-wrapper']//li[text()='Albany, NY - ALB']")
        itemToSelect.click()
        time.sleep(3)
        driver.quit()


ff = AutoComplete()
ff.test1()