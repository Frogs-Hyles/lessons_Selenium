import time
import math
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@pytest.mark.parametrize('lesson', [
    "236895", 
    "236896", 
    "236897", 
    "236898",
    "236899", 
    "236903", 
    "236904", 
    "236905"
    ]
    )
class TestLinks:

    answer = ""
    def test_lesssons(self, browser, lesson):
        link = f"https://stepik.org/lesson/{lesson}/step/1"
        browser.get(link)

        WebDriverWait(browser, 1200).until(
            EC.visibility_of_element_located((By.XPATH, '//a[text()="Войти"]'))
        )
        browser.find_element(By.XPATH, '//a[text()="Войти"]').click()
        WebDriverWait(browser, 1200).until(
            EC.visibility_of_element_located((By.XPATH, '//a[@data-tab-name="login"]'))
        )
        browser.find_element(By.XPATH, '//a[@data-tab-name="login"]').click()
        browser.find_element(By.XPATH, '//input[@name="login"]').send_keys(EMAIL)
        browser.find_element(By.XPATH, '//input[@name="password"]').send_keys(PASSWORD)

        browser.find_element(By.XPATH, '//button[text()="Войти"]').click()
        WebDriverWait(browser, 1200).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )
        browser.find_element(By.TAG_NAME, 'textarea').send_keys(math.log(int(time.time())))
        WebDriverWait(browser, 1200).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Отправить"]'))
        )
        browser.find_element(By.XPATH, '//button[text()="Отправить"]').click()
        WebDriverWait(browser, 120).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))
        )
        result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text

        if result != "Correct!": TestLinks.answer += result
        print(TestLinks.answer)
        assert result == "Correct!"
        
        
