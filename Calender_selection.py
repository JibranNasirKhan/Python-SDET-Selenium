from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class Auto_Select():
    def Keys1(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        Origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        Origin.click()
        Origin.send_keys("Pun")

        Origin1 = driver.find_elements(By.XPATH,"//div[@class='ac_results origin_ac']")
        print(len(Origin1))
        for city in Origin1:
            print(city.text)
            if "Pune (PNQ)" in city.text:
                city.click()
                time.sleep(2)
                break

        # Origin.send_keys(Keys.ENTER)
        # time.sleep(2)

        Arrival = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        Arrival.click()
        # time.sleep(2)
        Arrival.send_keys('bom')
        # time.sleep(2)
        Arrival1 = driver.find_elements(By.XPATH,"//li[@class='active ac_over']")
        print(len(Arrival1))
        for results in Arrival1:
            print(results.text)
            if "Mumbai (BOM)" in results.text:
                    results.click()
                    time.sleep(2)
                    break

        date = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        date.click()
        time.sleep(2)

        # driver.find_element(By.XPATH,"//td[@id='17/08/2022']").click()
        # time.sleep(2)

        All_date = driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody")
        time.sleep(2)
        for dates in All_date:
            if dates.get_attribute("data-date") == "22/08/2022":
                dates.click()
                time.sleep(4)
                break

dates = Auto_Select()
dates.Keys1()


