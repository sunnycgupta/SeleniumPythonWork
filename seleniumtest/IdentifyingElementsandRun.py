'''
Created on 15-Apr-2022

@author: sunny
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver=webdriver.Chrome(executable_path="/home/sunny/SeleniumSetup/chromedriver")
driver.implicitly_wait(10)
driver.get("http://demostore.supersqa.com/")
print(f"The title of driver is {driver.title}")

kart=driver.find_element(By.XPATH,"//*[starts-with(@id,'site-header')]")
print(type(kart))

print(kart.text)

valEnter=driver.find_element(By.ID,"woocommerce-product-search-field-0")
valEnter.send_keys("Hoodies")
valEnter.send_keys(Keys.ENTER)

pages=driver.find_elements(By.XPATH,"//*[contains(@class,'page_item')]")
print(len(pages))
myAccoumnt=driver.find_element(By.CSS_SELECTOR,".menu .nav-menu > li:nth-child(4) a")
myAccoumnt.click()

#driver.close()
