'''
Created on 16-Apr-2022

@author: sunny
'''

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="/home/sunny/SeleniumSetup/chromedriver")
driver.get("https://www.python.org/")
current_title=driver.title
expected_title="Welcome to Python.org"

if current_title != expected_title:
    print("Title of page is wrong {}".format(current_title))
    
current_link=driver.find_element(By.XPATH,"//a[@title='Python Package Index']")
current_link.click()

new_currenturl=driver.current_url
new_expectedurl="https://pypi.org/"

assert new_currenturl == new_expectedurl ,print(f" The title not matched {new_expectedurl}")

driver.close()