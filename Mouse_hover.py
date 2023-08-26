from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.yatra.com")
driver.maximize_window()
# driver.switch_to.alert.dismiss()
myaccount = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
Xplore = driver.find_element(By.XPATH,"//span[@class='more-arr']")
Mouse_hover = ActionChains(driver)
Mouse_hover.move_to_element(myaccount).perform()
time.sleep(2)
Mouse_hover.move_to_element(Xplore).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
time.sleep(40)

print("Task Complete")