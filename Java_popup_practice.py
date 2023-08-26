from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class first_task():
    def accept(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        driver.find_element(By.XPATH,"(//button[normalize-space()='Try it'])[1]").click()
        driver.switch_to.alert.accept()
        time.sleep(2)

        print("1st task done popup accepted")

poptask = first_task()
poptask.accept()


