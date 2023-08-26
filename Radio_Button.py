
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Radiobox_Value():
    def get_status(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(4)
        driver.find_element(By.ID, 'doi0').click()
        time.sleep(4)
        driver.find_element(By.ID, 'doi1').click()
        time.sleep(4)
        var1 = driver.find_element(By.ID, 'doi1').is_selected()
        print(var1)
        var2 = driver.find_element(By.ID, 'doi0').is_selected()
        print(var2)

status = Radiobox_Value()
status.get_status()