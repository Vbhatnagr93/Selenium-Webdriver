from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.HandyWrappers import HandyWrappers
import time



class ElementPresentCheck():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.implicitly_wait(10)

        hw = HandyWrappers(driver)

        driver.get(baseurl)


        elementResult1 = hw.isElementPresent("name", By.ID)
        print(str(elementResult1))


        elementResult2 = hw.elementPresenceCheck("//input[@id='name']", By.XPATH)
        print(str(elementResult2))


ff = ElementPresentCheck()
ff.test()

