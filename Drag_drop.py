from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://jqueryui.com/droppable/')
drag = ActionChains(driver)
driver.maximize_window()
driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
# drag.drag_and_drop(elem1,162,0).perform()
time.sleep(2)
elem1 = driver.find_element(By.ID,"draggable")
elem2 = driver.find_element(By.ID,"droppable")


drag.drag_and_drop(elem1,elem2).perform()
# drag.drag_and_drop(elem1,212,90).perform()
time.sleep(2)


print("Hooray")
