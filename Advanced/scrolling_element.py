from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollingElement():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        #Scroll Down
        driver.execute_script("window.scrollBy(0,800);")
        time.sleep(3)

        #Scroll Up
        driver.execute_script("window.scrollBy(0,-800);")
        time.sleep(3)


        #Scroll Element Into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-150);")


        #Native way to scroll element into view
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,-1000);")
        location = element.location_once_scrolled_into_view
        print("location: " +str(location))


ff = ScrollingElement()
ff.test()