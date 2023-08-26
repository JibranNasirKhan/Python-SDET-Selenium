from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

class Implcit():
    def Time_dynamic(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=in")
        driver.find_element(By.ID,"username").send_keys("machoman")
        driver.find_element(By.ID, "passwsssssord").send_keys("machoman")

#wait time for ID "username" will not wait for 10sec, However will wait for 10 sec as ID "password" will not be found as its garbage value n den give error

wait = Implcit()
wait.Time_dynamic()