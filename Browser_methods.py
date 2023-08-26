from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class BrowerMethod():
    def imp_methods(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://www.google.com/')
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.refresh()
        driver.find_element(By.CSS_SELECTOR, ".gb_d[data-pid='23']").click()
        time.sleep(4)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.fullscreen_window()
        time.sleep(2)
        driver.minimize_window()
        driver.quit()

method = BrowerMethod()
method.imp_methods()