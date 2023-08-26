from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://www.snapdeal.com/search?keyword=mobile&santizedKeyword=mobile&catId=0&categoryId=12&suggested=false&vertical=p&noOfResults=20&searchState=k3%3Dtrue%7Ck5%3D0%7Ck6%3D0%7Ck7%3DgGEgqdMAYAAAADoB%7Ck8%3D0&clickSrc=searchOnSubCat&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy#bcrumbSearch:mobile")
driver.maximize_window()
drag = ActionChains(driver)
elem1 = driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
elem2 = driver.find_element(By.XPATH,"//a[@class='price-slider-scroll right-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
# drag.move_to_element(elem1).drag_and_drop(50,0).perform()
# drag.move_to_element().pause(1).click_and_hold(elem1).move_by_offset(50,0).release().perform()
drag.click_and_hold(elem1).move_by_offset(50,0).release().perform()
time.sleep(2)
drag.click_and_hold(elem2).move_by_offset(-60,0).release().perform()

time.sleep(4)
print("Task done")


