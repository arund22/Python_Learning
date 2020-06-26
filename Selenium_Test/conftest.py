import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Browser_config():

    def browser(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        #driver = webdriver.Firefox()
        #driver = webdriver.Safari()
        #driver.set_page_load_timeout(20)
        driver.get(baseurl)
        #elementbyId = driver.find_element_by_id("name")
        elementbyId = driver.find_element(By.XPATH,"//*[@id='displayed-text']")

        if elementbyId is not None:
            print("Found an element by ID")
        else:
            print("Element by ID not found")

        elementbyName = driver.find_element(By.ID,"show-textbox")

        if elementbyName is not None:
            print("Found element by name")
        else:
            print("Element by name not found")


        mylelements = driver.find_elements_by_tag_name("td")

        length = len(mylelements)

        print(str(length))



        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.quit()

bb = Browser_config()
bb.browser()
