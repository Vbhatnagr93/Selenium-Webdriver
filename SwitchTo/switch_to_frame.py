from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        driver.execute_script("window.scrollBy(0,1000);")

        #Switch to frame using ID
        driver.switch_to.frame("courses-iframe")


        #Switch to frame using name
        # driver.switch_to.frame("iframe-name")

        #Switch to frame using numbers
        # driver.switch_to.frame(0) #index of frame
        time.sleep(2)

        #Search course
        searchBox = driver.find_element(By.ID, "search-courses")
        searchBox.send_keys("python")
        time.sleep(2)

        #Switch back to parent frame
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0,-1000);")
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Test Successful")


ff = SwitchToFrame()
ff.test()

