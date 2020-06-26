from selenium import webdriver
from selenium.webdriver.common.by import By

class Browse_Interactions():

    def browser_interactions(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        driver.maximize_window()

        # Get Title of Page:
        title = driver.title
        print(title)

        if 'Practice' in title:

            print("Title is correct")

        else:

            print("Title in incorrect")

        # Get CurrentURL of Page:
        cur_url = driver.current_url
        print(cur_url)

        if 'letskodeit' in cur_url:

            print("Url is correct")

        else:

            print("Url in incorrect")

        # Browser Refreshed:

        driver.refresh()
        print("Browser Refreshed")

        # Browser Refreshed:

        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")

        # Click on Object

        homepage = driver.find_element_by_xpath("//*[@class='navbar-brand header-logo']")
        homepage.click()
        print("Homepage clicked")


        # Browser_Back

        driver.back()

        print("driver went back")

        # Browser_Forward

        driver.forward()

        print("driver went fwd")

        # Click on Object

        homepage = driver.find_element_by_xpath("//*[@id='openwindow']")
        homepage.click()
        print("Window Opened")
        homepage = driver.find_element_by_xpath("//*[@class='navbar-brand header-logo']")
        homepage.click()
        print("Homepage clicked")

        pagesource = driver.page_source
        print(pagesource)

        # Window closed:

        # driver.close()

        #homepage = driver.find_element_by_xpath("//*[@id='openwindow']")
        #homepage.click()
        #print("Window Opened Again")
        #homepage = driver.find_element_by_xpath("//*[@class='navbar-brand header-logo']")
        #homepage.click()
        #print("Homepage clicked")

        # All Windows Closed:

        driver.quit()


run = Browse_Interactions()
run.browser_interactions()