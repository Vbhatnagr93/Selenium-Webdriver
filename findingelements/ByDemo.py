from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):

        baseurl = 'https://letskodeit.teachable.com/p/practice'

        driver = webdriver.Firefox()

        driver.get(baseurl)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("we found an element by ID")

        elementByXpath = driver.find_element(By.XPATH, ".//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by Xpath")

        elementByLinkText = driver.find_element(By.LINK_TEXT, "Login") #text of a link

        if elementByLinkText is not None:
            print("We found an element by Link text")

        elementByCss = driver.find_element(By.CSS_SELECTOR, "#name")

        if elementByCss is not None:
            print('We found an element by CSS')


ff = ByDemo()

ff.test()

#tag[id/class=''] - Find CSS elements
# input[id='displayed-text'] or
# #displayed-text or
# input#displayed-text

# input[class='displayed-text'] or
# .displayed-class or
# input.displayed-class

# concatenation of classes .class1.class2.class3 until we find a unique element

# for special characters tag[attribute<special character>='calue']