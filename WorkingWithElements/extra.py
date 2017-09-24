from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    
    def test(self):
        
        baseurl = "https://spacewalk-staging.herokuapp.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10) #this prompts for selenium to wait before trying to locate elements on the page
        
        loginLink = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        
        loginLink.click() #methods clicks the button
        
        
        emailField = driver.find_element(By.ID, "user_email")
        
        emailField.send_keys("testing+sw_gnobm2@revelry.co") #sends values to the input field
        
        
        passwordField = driver.find_element(By.ID, "user_password")
        
        passwordField.send_keys("password")
        
        
        time.sleep(3)
        
        emailField.clear()  #clears any input which was provided to input field
        
        time.sleep(3)


ff = ClickAndSendKeys()
ff.test()
