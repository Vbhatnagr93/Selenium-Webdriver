from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():

    def test(self):
        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.maximize_window()

        driver.get(baseurl)

        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")

        sel = Select(element)

        sel.select_by_value("benz")

        print("select benz by value")

        time.sleep(2)

        sel.select_by_index("2")

        print("select honda by index")

        time.sleep(2)

        sel.select_by_visible_text("BMW")

        print("select BMW by visible text")

        time.sleep(2)

        sel.select_by_index(2) #can also search by int instead of string

        print("select Honda by Index")


ff = DropdownSelect()

ff.test()