#myDIV

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class attr_Value():
    def get_Value(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        # driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        # ele = driver.find_element(By.CSS_SELECTOR,'#myDIV').is_displayed()
        # print(ele)
        # # After clicking "Toggle Hide/Show will the state of the element
        #
        # driver.find_element(By.CSS_SELECTOR, '.ws-btn.w3-hover-black.w3-dark-grey').click()
        # ele1 = driver.find_element(By.CSS_SELECTOR, '#myDIV').is_displayed()
        # print(ele1)

        driver.get('https://www.yatra.com/')
        driver.find_element(By.CSS_SELECTOR,'.icon.icon-angle-right.arrowpassengerBox').click()
        ele2 = driver.find_element(By.XPATH, "//span[@class='adultcount'][normalize-space()='1'] ").is_displayed()
        print(ele2)


        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//span[@class='demo-icon icon-hotels']").click()
        driver.find_element(By.XPATH,"//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)").click()
        ele3 = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(ele3)
        # driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > section:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > section:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)").click()
        # ele4 = driver.find_element(By.XPATH,"//select[@class='ageselect']]").is_displayed()
        # print(ele4)


view = attr_Value()
view.get_Value()