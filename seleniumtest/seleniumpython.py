'''
Created on 06-Sep-2021

@author: sunny
'''
from selenium import webdriver
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get("https://google.co.in")
driver.close()