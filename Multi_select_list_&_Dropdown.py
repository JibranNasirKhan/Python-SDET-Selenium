from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class Multi_Select():
    def demo_multiselect(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("website changed")
        driver.maximize_window()
        dd_Demo = driver.find_element(By.CLASS_NAME, 'ddn-parent').click()
        dd_Demo = driver.find_element(By.CLASS_NAME, "borderRadius").click()
        dd_Demo = driver.find_element(By.CLASS_NAME, 'custom-check').click()
        dd = Select(dd_Demo)
        time.sleep(5)
        dd.select_by_index(1)


Run = Multi_Select()
Run.demo_multiselect()