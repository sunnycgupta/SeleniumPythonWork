'''
Created on 16-Apr-2022

@author: sunny
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException


def open_browser():
    driver=webdriver.Chrome(executable_path="/home/sunny/SeleniumSetup/chromedriver")
    driver.implicitly_wait(10)
    return driver

def go_to_demosite(driver):
    driver.get("http://demostore.supersqa.com/")
    actual_page_title=driver.title
    expected_page_title="Demo Store – Practice Automation The Right Way"
    if actual_page_title==expected_page_title:
        print("Pass")


def add_first_item(driver):
    first_element=driver.find_element(By.CSS_SELECTOR,".button.product_type_simple.add_to_cart_button.ajax_add_to_cart")
    first_element.click()
    

def go_to_cart(driver):
    driver.get("http://demostore.supersqa.com/cart")
    
def apply_fake_coupon(driver,coupon_name):
    coupon_field=driver.find_element(By.ID,"coupon_code")
    coupon_field.send_keys(coupon_name)
    apply_btn=driver.find_element(By.NAME,"apply_coupon")
    apply_btn.click()
    
def check_cart_value(driver):
    
    for x in range(5):
        try:
            driver.find_element(By.CLASS_NAME,"woocommerce-cart-form__cart-item.cart_item")
            return 
        except NoSuchElementException:
            print("Element is not present")
            time.sleep(2)
            driver.refresh()

def check_error(driver):
    return driver.find_element(By.CSS_SELECTOR,".woocommerce-notices-wrapper > .woocommerce-error > li").text




def close_browser(driver):
    driver.close()




if __name__ == '__main__':
    driver=open_browser()
    go_to_demosite(driver)
    add_first_item(driver)
    go_to_cart(driver)
    check_cart_value(driver)
    apply_fake_coupon(driver,"fake")
    expected_error=check_error(driver)
    print(expected_error)
    actual_error='Coupon "fake" does not exist!'
    assert actual_error==expected_error,"Error doesnot exist"
    close_browser(driver)
    
    
    
    
    