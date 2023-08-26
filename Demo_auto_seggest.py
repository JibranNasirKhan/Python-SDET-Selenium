from selenium import webdriver
from selenium.webdriver import Keys
import selenium.webdriver.common.keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class Auto_Sugg():
    def select(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        driver.maximize_window()
        depart = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart.click()
        time.sleep(2)
        depart.send_keys('Pune')
        time.sleep(4)
        depart.send_keys(Keys.ENTER)
        time.sleep(2)
        arrival = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        arrival.click()
        arrival.send_keys("New")
        time.sleep(2)
        search = driver.find_elements(By.CLASS_NAME,"ac_results")
        print(len(search))
        for results in search:
            if "New York (JFK)" in results.text:
                results.click()
                time.sleep(4)
                break

run = Auto_Sugg()
run.select()
