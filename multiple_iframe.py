

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
driver.maximize_window()
time.sleep(20)
# driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
# //iframe[@id='iframeResult']
driver.switch_to.frame(0)
# driver.switch_to.frame("iframeResult")
driver.find_element(By.XPATH,"//a[normalize-space()='Not Sure Where To Begin?']").click()
time.sleep(4)