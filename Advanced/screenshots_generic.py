from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/"

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abc")
        driver.find_element(By.NAME, "commit").click()
        self.takeScreenshot(driver)

        #destfilename = "c://username/desktop..." For windows users


    def takeScreenshot(self, driver):
            """
            Take screenshot of the current open web page
            :param self:
            :param driver:
            :return:
            """
            fileName = str(round(time.time() * 1000)) + ".png"
            screenshotDirectory = "/Users/revelrycomputer/desktop/"
            destinationFile = screenshotDirectory + fileName

            try:

                driver.save_screenshot(destinationFile)
                print("Screenshot saved to directory" + destinationFile)
            except NotADirectoryError:
                print("Not a directory issue")

ff = Screenshots()
ff.test()