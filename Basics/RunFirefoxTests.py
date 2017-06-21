from selenium import webdriver  #import the webdriver from selenium package

class RunFFtests():
    def test(self):
        driver = webdriver.Firefox()  #  # create an instance of the webdriver

        driver.get("http://www.letskodeit.com") #to open the url


FF = RunFFtests()

FF.test()




