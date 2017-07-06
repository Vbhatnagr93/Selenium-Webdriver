from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class getText():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get(baseurl)

        openTabElement = driver.find_element(By.ID, "opentab")

        eleText = openTabElement.text #property to get the text name on the element

        print("Text on element is: " +str(eleText))

        time.sleep(1)

        driver.quit()




ff = getText()

ff.test()
