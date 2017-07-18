from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToAlert():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)


        driver.find_element(By.ID, "name").send_keys("Vivek")
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)
        alert1 = driver.switch_to.alert #switches to the alert message
        alert1.accept() #clicks on the OK button when the alert is shown
        time.sleep(2)
        driver.find_element(By.ID, "name").send_keys("Kumar")
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss() #Clicks the CANCEL button when the alert is shown


ff = SwitchToAlert()
ff.test()