from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.HandyWrappers import HandyWrappers
import time



class UsingWrappers():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)

        driver.get(baseurl)

        textField = driver.find_element(By.ID, "name")
        textField.send_keys("Test")

        time.sleep(2)

        textField2 = hw.getElement("//input[@id='name']", locatorType="xpath") #We do not have to findelement by
        


ff = UsingWrappers()

ff.test()