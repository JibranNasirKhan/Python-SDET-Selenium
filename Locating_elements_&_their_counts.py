from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

class Number_of_anchor():
    def archors(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://yatra.com')
        taga = driver.find_elements(By.TAG_NAME,'a')
        for i in taga:
            print(i.text)
        print(len(taga()))
        time.sleep(4)

anch = Number_of_anchor()
anch.archors()