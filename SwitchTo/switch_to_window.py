from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)

        driver.implicitly_wait(3)

        #Find parent handle --> Main window
        parentHandle = driver.current_window_handle #A property not a method
        print("Parent Handle: " +parentHandle)

        #Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()


        #Find all available handles, there should be two handles after clicking open window button
        handles = driver.window_handles

        #switch to window and search course
        for handle in handles:
            print("Handle: " +handle)
            if handle not in parentHandle:
                driver.switch_to.window(handle)
                print("Switched to window:: " + handle )
                searchBox = driver.find_element(By.ID, "search-courses")
                searchBox.send_keys("python")
                time.sleep(2)
                driver.close() #just closes the current window in focus
                break


        #Switch back to parent Handle
        driver.switch_to.window(parentHandle)
        driver.find_element(By.ID, "name").send_keys("Test Successful")


ff = SwitchToWindow()
ff.test()