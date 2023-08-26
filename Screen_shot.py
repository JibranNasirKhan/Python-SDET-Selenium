from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class SS():
    def screenshot(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        driver.get_screenshot_as_file("E:\\Python Selenium\\Selenium\\LearningSelenium\\1st.png")
        email_demo = driver.find_element(By.XPATH,"//input[@id='login-input']")
        time.sleep(2)
        # email_demo.screenshot("E:\\Python Selenium\\Selenium\\LearningSelenium\\1st.png")
        time.sleep(2)
        email_demo.send_keys("hurray")
        email_demo.send_keys(Keys.ENTER)
        driver.get_screenshot_as_file("E:\\Python Selenium\\Selenium\\LearningSelenium\\2nd.png")
        driver.save_screenshot("E:\\Python Selenium\\Selenium\\LearningSelenium\\error.png")

Screenshot_demo = SS()
Screenshot_demo.screenshot()
