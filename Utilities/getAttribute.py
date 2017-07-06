from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class getAttribute():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get(baseurl)


        element = driver.find_element(By.ID, "name")

        result = element.get_attribute("placeholder") #This command gets and stores the attribute value like classname, id name, etc

        print("Attribute is: " +str(result))


ff = getAttribute()

ff.test()