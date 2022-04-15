'''
Created on 06-Sep-2021

@author: sunny
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Firefox()
driver.get("https://google.co.in")
driver.close()