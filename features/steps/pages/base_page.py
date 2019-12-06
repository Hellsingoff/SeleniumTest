from selenium.common.exceptions import InvalidArgumentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        try:
            self.browser.get(self.url)
        except InvalidArgumentException:
            raise AssertionError('Не удалось открыть сайт')

    def is_present(self, locator, timer=10):
        try:
            wait = EC.presence_of_element_located(locator)
            element = WebDriverWait(self.browser, timer).until(wait)
            return element
        except TimeoutException:
            raise AssertionError('Элемент не найден')

    def is_clickable(self, locator, timer=10):
        try:
            wait = EC.element_to_be_clickable(locator)
            element = WebDriverWait(self.browser, timer).until(wait)
            return element
        except TimeoutException:
            raise AssertionError('Элемент не активен или отсутствует')

    def click_gently(self, locator, timer=10):
        self.is_clickable(locator).click()

    def check_url(self, url):
        return url.lower() == self.browser.current_url
