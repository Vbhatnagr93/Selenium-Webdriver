from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Utilities.HandyWrappers import HandyWrappers
import time



class DynamicXPathFormat():

    def test(self):
        baseurl = "https://letskodeit.teachable.com"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.implicitly_wait(10)

        driver.get(baseurl)


        #Dynamic Xpath takes input dynamically and finds elements

        driver.find_element(By.LINK_TEXT, "Login").click()
        email = driver.find_element(By.ID, "user_email")
        email.send_keys("test@email.com")

        password = driver.find_element(By.ID, "user_password")
        password.send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()


        #search for courses
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("Javascript")

        #select course
        _course = "//div[contains(@class, 'course-listing-title') and contains(text(),'{0}')]"  #here is where xpath is added in place of {0}
        _courseLocator = _course.format("JavaScript for beginners") #this replaces {0} with search string

        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()


ff = DynamicXPathFormat()
ff.test()

