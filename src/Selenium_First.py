import pytest
from selenium import webdriver

@pytest.fixture
def browser():

    driver = webdriver.Chrome('/anaconda3/lib/python3.7/selenium/webdriver/chrome/chromedriver')
    driver.set_page_load_timeout(20)
    driver.get("http://www.google.com")
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.quit()

