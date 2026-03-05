import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        # ждём появления alert
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())

        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs(12 * math.sin(float(x)))))
        alert.send_keys(answer)
        alert.accept()

        try:
            WebDriverWait(self.browser, 10).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            print(f"Your code: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


# =========================
# ProductPage
# =========================
class ProductPage(BasePage):

    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages .alert-info strong")

    def add_product_to_basket(self):
        self.browser.find_element(*self.ADD_TO_BASKET_BUTTON).click()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_correct_product_name(self, expected_name):
        actual_name = self.browser.find_element(*self.SUCCESS_MESSAGE).text
        assert actual_name == expected_name, \
            f"Ожидалось название '{expected_name}', получено '{actual_name}'"

    def should_be_correct_product_price(self, expected_price):
        actual_price = self.browser.find_element(*self.BASKET_TOTAL).text
        assert actual_price == expected_price, \
            f"Ожидалась цена '{expected_price}', получена '{actual_price}'"


# =========================
# Запуск теста
# =========================
if __name__ == "__main__":
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    browser = webdriver.Chrome()
    page = ProductPage(browser, link)

    try:
        page.open()

        # берём реальные данные товара
        product_name = page.get_product_name()
        product_price = page.get_product_price()

        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        # проверяем
        page.should_be_correct_product_name(product_name)
        page.should_be_correct_product_price(product_price)

        print("Тест выполнен успешно!")

    finally:
        time.sleep(5)  # чтобы увидеть результат
        browser.quit()