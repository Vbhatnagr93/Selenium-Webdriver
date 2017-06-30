from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckboxes():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseurl)

        driver.implicitly_wait(10)

        RadioButton1 = driver.find_element(By.ID, "bmwradio") #click the radio button
        RadioButton1.click()

        time.sleep(2)

        RadioButton2 = driver.find_element(By.ID, "benzradio") #click another radio button
        RadioButton2.click()

        time.sleep(2)

        Checkbox1 = driver.find_element(By.ID, "bmwcheck")  # click the checkbox
        Checkbox1.click()

        time.sleep(2)

        Checkbox2 = driver.find_element(By.ID, "benzcheck")  # click another checkbox
        Checkbox2.click()

        print("Radio button1 is selected? " +str(RadioButton1.is_selected())) #true if selected, false if not
        print("Radio button2 is selected? " + str(RadioButton2.is_selected()))
        print("Check box1 is selected? " + str(Checkbox1.is_selected()))
        print("Check box2 is selected? " + str(Checkbox2.is_selected()))
        


ff = RadioButtonsAndCheckboxes()

ff.test()

