from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
achains = ActionChains(driver)
rightclick = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
elem1 = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']")
achains.context_click(rightclick).perform()
time.sleep(2)
elem1.click()

time.sleep(4)
driver.switch_to.alert.accept()

doubleclick = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
achains.double_click(doubleclick).perform()
time.sleep(4)
# driver.switch_to.alert.accept()

print("Task Complete")

