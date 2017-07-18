from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering():
    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        driver.execute_script("window.scrollBy(0,800);")
        time.sleep(2)
        element = driver.find_element(By.ID, "mousehover")
        itemToClickLocator = ".//div[@class='mouse-hover-content']//a[text()='Top']"

        try:
            actions = ActionChains(driver)
            actions.move_to_element(element).perform() #searches for element and performs action on it like hover
            print("Mouse Hovered on element")
            time.sleep(2)
            topLink = driver.find_element(By.XPATH, itemToClickLocator)
            # actions.move_to_element(topLink).perform()
            topLink.click()
            print("Item Clicked")
        except:
            print("Mouse Hover failed on Element")

        time.sleep(3)
        driver.quit()


ff = MouseHovering()
ff.test()