from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CLASS_NAME, "form-control.first:required")
    input2 = browser.find_element(By.CLASS_NAME, "form-control.second:required")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third:required")

    input1.send_keys("Заполено")
    input2.send_keys("Заполено")
    input3.send_keys("Заполено")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()