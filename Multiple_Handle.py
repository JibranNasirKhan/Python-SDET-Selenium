from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.yatra.com")
driver.maximize_window()
time.sleep(2)
first_handle = driver.current_window_handle
print(first_handle)
driver.find_element(By.XPATH,"//a[@title='Yatra Gift Cards']//img[@class='conta iner large-banner']").click()
all_handle = driver.window_handles
print(all_handle)

for handle in all_handle:
    if handle != first_handle:
        driver.switch_to.window(handle)

driver.find_element(By.XPATH,"//a[@class='shop_now']").click()
second_handle = driver.current_window_handle
print(second_handle)

second_Set_tab = driver.window_handles
print(second_Set_tab)

for tabs in second_Set_tab:
    if tabs != second_Set_tab:
        driver.switch_to.window(tabs)

time.sleep(4)
amount = driver.find_element(By.XPATH, "//label[normalize-space()='Enter Amount*']")
time.sleep(2)
amount.click()
amount.send_keys("25")
time.sleep(2)

driver.switch_to.window(first_handle)
driver.switch_to.window(second_handle)

time.sleep(4)