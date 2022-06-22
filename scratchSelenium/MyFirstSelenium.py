
from selenium  import webdriver

driver=webdriver.Chrome("/usr/local/bin/chromedriver")
driver.set_page_load_timeout(30)
driver.get("https://www.facebook.com/")
driver.implicitly_wait(20)
driver.maximize_window()
print(driver.title)
assert "Fpacebook" in driver.title
driver.find_element_by_id("email").send_keys("Selenium")
driver.find_element_by_name("pass").send_keys("password")
driver.find_element_by_name("login").click()
driver.get_screenshot_as_file("facebook.png")

driver.close()