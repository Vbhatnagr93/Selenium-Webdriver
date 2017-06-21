from selenium import webdriver

class FindByXpathCss():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.get(baseUrl)

        elementByXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementByXpath is not None:
            print("we found an element by xpath")

        elementByCss = driver.find_element_by_css_selector("#name")

        if elementByCss is not None:
            print("We found an element by CSS")


ff = FindByXpathCss()

ff.test()