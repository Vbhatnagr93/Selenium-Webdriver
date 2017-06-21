from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):

        baseurl = 'https://letskodeit.teachable.com/p/practice'

        driver = webdriver.Firefox()

        driver.get(baseurl)

        elementListByClassName = driver.find_elements_by_class_name("inputs") #this is to find multiple elements
        length = len(elementListByClassName)

        if elementListByClassName is not None:
            print("ClassName --> Size of the list is: " +str(length))

        elementListByTagName = driver.find_elements(By.TAG_NAME, "h1")
        length2 = len(elementListByTagName)

        if elementListByTagName is not None:
            print("TagName --> Size of the list is: " +str(length2))


ff = ListOfElements()

ff.test()

