import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(int(x))

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.ID, "robotCheckbox").click()
    button = browser.find_element(By.XPATH, '//button[text()="Submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.ID, "robotsRule").click()
    button.click()
finally:
    time.sleep(5)
    browser.quit()
