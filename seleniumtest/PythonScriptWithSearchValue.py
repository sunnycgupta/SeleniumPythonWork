'''
Created on 16-Apr-2022

@author: sunny
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="/home/sunny/SeleniumSetup/chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.python.org/")
currentTitle=driver.title
expectedTitle="Welcome to Python.org"

if currentTitle == expectedTitle :
    print("Successull landing")
else:
    raise Exception(f"Not on the exoected page {currentTitle}") 

search_text="id-search-field"
search_text_field=driver.find_element(By.ID,search_text)
search_text_field.send_keys("Testing")

submit_button_text="submit"
submit_button_text_ele=driver.find_element(By.NAME,submit_button_text)
submit_button_text_ele.click()


xpathresult="//*[@id='content']/div/section/form/ul/li[1]"
xpathresult_ele=driver.find_element(By.XPATH,xpathresult)
assert xpathresult_ele.is_displayed(),f"Values are absent"
driver.close()