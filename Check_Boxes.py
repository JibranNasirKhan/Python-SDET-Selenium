
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class checkbox_Value():
    def get_status(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://in.search.yahoo.com/?fr2=inr')
        driver.maximize_window()
        driver.find_element(By.XPATH,"//div[@title='Sign In']").click()
        time.sleep(2)
        check = driver.find_element(By.CSS_SELECTOR,"label[for='persistent']").is_selected()
        print(check)
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "label[for='persistent']").click()
        time.sleep(2)
        check2 = driver.find_element(By.CSS_SELECTOR, "label[for='persistent']").is_selected()
        print(check2)


        # driver.find_element(By.XPATH, "//input[@id='interest_sell_c0']").click()
        # time.sleep(2)
        # check3 = driver.find_element(By.XPATH, "//input[@id='interest_sell_c0']").is_selected()
        # print(check3)

box = checkbox_Value()
box.get_status()