
"""
driver = webdriver.Chrome(executable_path="")  if the drive is not in system path
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com/")
print(f"The title in chrome is {driver.title}")
driver.close()


driver=webdriver.Firefox()
driver.get("http://demostore.supersqa.com/")
print(f"The title fetched in firefox is {driver.title}")
driver.close()