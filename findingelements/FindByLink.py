from selenium import webdriver

class FindByLink():
    def test(self):

        baseUrl = "https://letskodeit.teachable.com/p/practice"

        driver = webdriver.Firefox()

        driver.get(baseUrl)

        elementByLink = driver.find_element_by_link_text("Login")

        if elementByLink is not None:
            print("We found an element by link text")

        elementByPartialLink = driver.find_element_by_partial_link_text("Prac")

        if elementByPartialLink is not None:
            print("We found an element by partial link")


ff = FindByLink()

ff.test()