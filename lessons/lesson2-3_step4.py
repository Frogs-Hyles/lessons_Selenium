from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
finally:
    time.sleep(5)
    browser.quit()