from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def testListOfElements(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseurl)

        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type, 'radio') and contains(@name,'cars')]")


        size = len(radioButtonsList)

        print(size)

        for radioButton in radioButtonsList:

            isSelected = radioButton.is_selected()

            if not isSelected:

                radioButton.click()
                time.sleep(2)


ff = WorkingWithElementsList()

ff.testListOfElements()