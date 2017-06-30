from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HiddenElements():

    def test(self):

        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseurl)

        driver.implicitly_wait(2)


        textBoxElement = driver.find_element_by_id("displayed-text")

        textBoxState = textBoxElement.is_displayed() #true if visible, false if hidden
        #Exception if not present in DOM
        print("Text is Visible?" +str(textBoxState))
        time.sleep(2)

        # Click the Hide button
        driver.find_element_by_id("hide-textbox").click()


        #find state of the box
        textBoxState = textBoxElement.is_displayed()
        print("Text is Visible?" + str(textBoxState))
        time.sleep(2)


        #click the showbutton
        driver.find_element_by_id("show-textbox").click()



        #find the state of the text box
        textBoxState = textBoxElement.is_displayed()
        print("Text is Visible?" + str(textBoxState))
        time.sleep(2)

        #browser close
        driver.quit()


    def testExpedia(self):

        baseurl = "https://www.expedia.com"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseurl)

        driver.implicitly_wait(2)

        driver.find_element_by_id("tab-flight-tab-hp").click()

        dropDownElement = driver.find_element_by_id("flight-age-select-1")

        print("Element is visible?" +str(dropDownElement.is_displayed()))

ff = HiddenElements()

ff.test()

ff.testExpedia()

