from selenium.webdriver.common.by import By

class GooglePageLocators():
    SEARCH_FIELD = (By.NAME, 'q')
    SEARCH_BUTTON = (By.NAME, 'btnK')

class CBRPageLocators():
    RECEPTION = (By.CSS_SELECTOR, '.header .important-links__item_ip > a')
    GRATITUDE = (
            By.CSS_SELECTOR, '.reception_type_container > div:nth-child(3)')
    GRATITUDE_MESSAGE = (By.NAME, 'MessageBody')
    AGREEMENT = (By.NAME, 'Agreement')
    BURGER = (By.CSS_SELECTOR, '.header .burger')
    ABOUT = (By.CSS_SELECTOR, 'li.for_branch_11377 > a')
    WARNING = (By.CSS_SELECTOR, '[data-catalogid="11380"] > div > a')
    WARNING_TEXT = (By.CSS_SELECTOR, '#content p')
    EN_LANG = (By.CSS_SELECTOR, '.header .langs > li:nth-child(2) > a')