from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os 

current_dir = os.path.abspath(os.path.dirname(__file__))
try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input2 = browser.find_element(By.NAME, "lastname")
    input3 = browser.find_element(By.NAME, "email")

    input1.send_keys("Иван")
    input2.send_keys("Иванов")
    input3.send_keys("iivanov@mail.ru")
    
    file_path = os.path.join(current_dir, 'file.txt')
    browser.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(file_path)
    browser.find_element(By.XPATH, '//button[text()="Submit"]').click()

finally:
    time.sleep(10)
    browser.quit()