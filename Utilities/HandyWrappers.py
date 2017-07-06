from selenium import webdriver
from selenium.webdriver.common.by import By


class HandyWrappers():

    def __init__(self, driver):

        self.driver = driver


    def getByType(self, locatorType):

        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "classname":
            return By.CLASS_NAME
        elif locatorType == "Linktext":
            return By.LINK_TEXT
        elif locatorType == "xpath":
            return By.XPATH
        else:
            print("Locator type is not supported")
        return False


    def getElement(self, locator, locatorType="id"):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element is found")
        except:
            print("Element not found")

            return element


    def isElementPresent(self, locator, byType):

        try:
           element = self.driver.find_element(byType, locator)
           if element is not None:
               print("Element is found")
               return True

           else:
               print("Element not found")
               return False

        except:
            print("Element not found")
            return False



    def elementPresenceCheck(self, locator, byType):
        try:
            elementsList = self.driver.find_elements(byType, locator)
            if len(elementsList) > 0:
                print("Element is found")
                return True

            else:
                return False

        except:
            print("Element not found")
            return False