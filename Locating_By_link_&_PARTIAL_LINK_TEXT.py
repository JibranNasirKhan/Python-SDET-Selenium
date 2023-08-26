# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# class locate_by_link_Element():
#     def locate_by_link(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get('https://yatra.com/')
#         driver.maximize_window()
#         driver.find_element(By.LINK_TEXT, 'Yatra for Business').click()
#         time.sleep(20)
#
# findbylink = locate_by_link_Element()
# findbylink.locate_by_link()


# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# class Locate_by_partial_Link():
#     def locate_by_partial_link(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://yatra.com/")
#         driver.maximize_window()
#         driver.find_element(By.PARTIAL_LINK_TEXT, 'Yatra for').click()
#         time.sleep(10)
#
# findpartial = Locate_by_partial_Link()
# findpartial.locate_by_partial_link()

import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Locate_by_partial_Link():
    def locate_by_partial_link(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://yatra.com/")
        driver.maximize_window()
        driver.find_element(By.PARTIAL_LINK_TEXT, 'Holida').click()
        time.sleep(10)

findpartial = Locate_by_partial_Link()
findpartial.locate_by_partial_link()