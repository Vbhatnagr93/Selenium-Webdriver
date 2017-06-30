from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()

        #window maximize

        driver.maximize_window()

        #open the url

        driver.get(baseUrl)

        #Get title

        title = driver.title

        print("Title is: " +title)

        #Get current Url

        currentUrl = driver.current_url

        print("Current Url is: " +currentUrl )

        #Browser refresh

        driver.refresh()

        print("Browser refreshed first time")

        driver.get(driver.current_url)

        print("Browser refreshed second time")

        #open another url

        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")

        currentUrl = driver.current_url

        print("Current Url is: " + currentUrl)

        #Browser back

        driver.back()

        print("Went one step back in browser history")

        currentUrl = driver.current_url

        print("Current Url is: " + currentUrl)

        #browser forward

        driver.forward()

        print("One step forward in browser history")

        currentUrl = driver.current_url

        print("Current Url is: " + currentUrl)

        #page source

        pageSource = driver.page_source

        #Browser close/Quit

        #driver.close()

        driver.quit()


ff = BrowserInteractions()

ff.test()




