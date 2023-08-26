# import time
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
#
# class Locate_Tag_Name():
#     def locatetagname(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
#         driver.maximize_window()
#         driver.find_element(By.TAG_NAME, "input").send_keys("test@test.com")
#         time.sleep(10)
#
# locate = Locate_Tag_Name()
# locate.locatetagname()


import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# """"Locating by class name, There are 3 class names in that tag seperated by spaces we need to take only one out of it"""
# class name in inspect gives u "yt-sme-mobile-input required_field email-login-box" but we need to take the unique one which is "email-login-box"

class Locate_by_class_name():
    def Class_Name_tag(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,'email-login-box').send_keys('test@test.com')
        time.sleep(10)

findclass = Locate_by_class_name()
findclass.Class_Name_tag()
