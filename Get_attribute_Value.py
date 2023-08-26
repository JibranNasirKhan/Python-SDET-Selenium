from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class attr_Value():
    def get_Value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        attr = driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute('id')
        attr1 = driver.find_element(By.CLASS_NAME, 'js-footer-new').get_attribute('class')
        print(attr)
        print(attr1)
        time.sleep(2)

prAttr = attr_Value()
prAttr.get_Value()