from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Locate_Element_txt():
    def Element_text(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME, "icon-holidays").click()
        time.sleep(2)
        text = driver.find_element(By.XPATH, "//h1[normalize-space()='Book Domestic and International Holidays']").text
        driver.find_element(By.XPATH,"//span[normalize-space()='Hotels']").click()
        text1 = driver.find_element(By.CLASS_NAME, 'mainAboutHead').text
        print(text)
        print(text1)
        time.sleep(2)

textp = Locate_Element_txt()
textp.Element_text()
