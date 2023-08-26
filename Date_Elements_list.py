from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class kayak():
    def Auto_suggest(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.ixigo.com/flights")
        driver.maximize_window()
        time.sleep(5)
        # driver.find_element(By.XPATH, "//*[name()='path' and contains(@d,'M18 6L12 1')]").click()
        # time.sleep(4)
        Dep_city = driver.find_element(By.XPATH, "//div[@class='orgn u-ib u-v-align-bottom u-text-left']//input[@placeholder='Enter city or airport']")
        # Dep_city = driver.find_element(By.CSS_SELECTOR, "input[placeholder='From?']")
        Dep_city.click()
        Dep_city.send_keys("Pun")
        Dep_city.send_keys(Keys.ENTER)
        time.sleep(2)

        Arr_city = driver.find_element(By.XPATH, "//div[@class='dstn u-ib u-v-align-bottom u-text-left']//input[@placeholder='Enter city or airport']")
        Arr_city.click()
        Arr_city.send_keys("del")
        Arr_city.send_keys(Keys.ENTER)

        Dep_Date = driver.find_elements(By.XPATH,"//input[@placeholder='Depart']")
        time.sleep(2)
        for date in Dep_Date:
            if date.get_attribute("data-date") == "12082022":
                date.click()
                time.sleep(4)
                break


run = kayak()
run.Auto_suggest()