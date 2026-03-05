from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, 'num1').text)
    y = int(browser.find_element(By.ID, 'num2').text)

    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f'[value="{x+y}"]').click()
 
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()
finally:
    time.sleep(5)
    browser.quit()