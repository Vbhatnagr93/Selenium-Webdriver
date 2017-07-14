from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.HandyWrappers import HandyWrappers
import time


class ImplicitWaitDemo():
    def test(self):
        baseurl = "https://letskodeit.teachable.com"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.implicitly_wait(10) #this wait is applied to driver instance so all elements we're trying to find, use this

        driver.get(baseurl)

        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        loginLink.click()

        emailField = driver.find_element(By.ID, "user_email")
        emailField.send_keys("test")


ff = ImplicitWaitDemo()
ff.test()