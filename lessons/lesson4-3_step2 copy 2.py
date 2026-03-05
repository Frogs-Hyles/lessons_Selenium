import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException


# =========================
# BasePage
# =========================
class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()

        try:
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


# =========================
# ProductPage
# =========================
class ProductPage(BasePage):

    # Локаторы
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")

    # Действия
    def add_product_to_basket(self):
        button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        button.click()

    # Получение данных
    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    # Проверки
    def should_be_correct_product_name_in_message(self):
        product_name = self.get_product_name()
        success_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text

        assert product_name == success_name, \
            f"Ожидалось '{product_name}', но получили '{success_name}'"

    def should_be_correct_product_price_in_message(self):
        product_price = self.get_product_price()
        basket_price = self.browser.find_element(*self.BASKET_TOTAL).text

        assert product_price == basket_price, \
            f"Ожидалась цена '{product_price}', но получили '{basket_price}'"


# =========================
# Fixture
# =========================
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


# =========================
# Test
# =========================
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_correct_product_name_in_message()
    page.should_be_correct_product_price_in_message()