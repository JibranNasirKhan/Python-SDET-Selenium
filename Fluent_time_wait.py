from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class Implcit():
    def Time_dynamic(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("")