
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

class Dropdown_Value():
    def get_status(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()

        driver.find_element(By.XPATH,'//button[text()="Accept All Cookies"]')
        dropdown = driver.find_element(By.NAME,"UserTitle").click()
        dd = Select(dropdown)
        dd.select_by_value("Customer_Service_Manager_AP")
        time.sleep(3)
        dd.select_by_index(1)
        dd.select_by_visible_text("Operations_Manager_AP")



status = Dropdown_Value()
status.get_status()