from selenium import webdriver

class FindByClassTag():

    def test(self):

        baseurl = "https://letskodeit.teachable.com/pages/practice"

        driver = webdriver.Firefox()

        driver.get(baseurl)

        elementByclassName = driver.find_element_by_class_name("displayed-class") #initialize
        elementByclassName.send_keys("Testing the Element") #sends a value to be filled

        if elementByclassName is not None:

            print("We found an element by class name")

        elementByTagName = driver.find_element_by_tag_name("h1")
        text = elementByTagName.text #puts the header text into the text variable

        if elementByTagName is not None:

            print("We found an element by Tag Name and text on element is: " +str(text)) #text is also printed


ff = FindByClassTag()

ff.test()

