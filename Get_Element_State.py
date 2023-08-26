from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class attr_Value():
    def get_Value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://training.openspan.com/login')
        state = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(state)
        # Mentioning info in username and password to check if login-button highlights
        driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys('test')
        driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys('test')
        state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state1)

getstate = attr_Value()
getstate.get_Value()
