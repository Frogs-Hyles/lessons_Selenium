from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element([By.ID, "price"], "$100")
    )
    
    browser.find_element(By.ID, 'book').click()
    
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
finally:
    time.sleep(5)
    browser.quit()