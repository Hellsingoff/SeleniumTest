from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage

class GooglePage(BasePage):
    found = {}
    def find_link(self, url):
        try:
            url = url.lower()
            self.found[url] = self.browser.find_element_by_css_selector(
                                            '[href$="%s/"]' % url.lower())
        except NoSuchElementException:
            raise AssertionError('Ссылка не найдена на странице')

    def go_to_selected_result(self, url):
        assert url.lower() in self.found, 'Ссылки нет в локаторах'
        try:
            self.found[url.lower()].click()
            # На случай открытия страницы в новой вкладке:
            self.browser.switch_to_window(self.browser.window_handles[-1])
        except:
            raise AssertionError('Ссылка найдена, но переход не удался')