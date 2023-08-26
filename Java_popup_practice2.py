from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
driver.switch_to.alert.send_keys("Jibran Nasir Khan")
driver.switch_to.alert.accept()
time.sleep(4)

print("All task completed")

