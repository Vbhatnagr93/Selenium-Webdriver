from selenium import webdriver
from selenium.webdriver.common.by import By

class FindPrice():
    def test(self):

        baseurl = "http://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.get(baseurl)

        elementById = driver.find_element(By.XPATH, ".//*[@id='product']/tbody/tr[3]/td[3]")

        if elementById is not None:

            print("value of python prog lang is " +str(elementById))

        else:
            print("Element not found")


price = FindPrice()

price.test()



