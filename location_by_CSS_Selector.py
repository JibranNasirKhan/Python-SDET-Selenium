import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Find_CSS_Selector():
    def locate_elements_by_CSS(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys("test@test.com")
        time.sleep(10)

findcss = Find_CSS_Selector()
findcss.locate_elements_by_CSS()