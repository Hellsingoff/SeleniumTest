from .base_page import BasePage

class CBRPage(BasePage):
    def warning_memory(self, locator):
        return self.is_present(locator).text

    def check_warning(self, locator):
        return self.warning_text != self.warning_memory(locator)
