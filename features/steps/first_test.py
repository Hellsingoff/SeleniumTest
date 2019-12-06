import behave
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidArgumentException
from pages.google_page import GooglePage
from pages.cbr_page import CBRPage
from pages.locators import GooglePageLocators
from pages.locators import CBRPageLocators

@given('открыть сайт google.ru')
def step(context):
    context.page = GooglePage(context.browser, 'https://www.google.ru/')
    context.page.open()
    assert context.page.check_url('https://www.google.ru/'), 'Не тот сайт'

@then('проверить, что появилось поле поиск')
def step(context):
    context.page.is_present(GooglePageLocators.SEARCH_FIELD)

@then('ввести в поле поиск значение "{text}"')
def step(context, text):
    try:
        field = context.browser.find_element(*GooglePageLocators.SEARCH_FIELD)
        field.send_keys(text)
    except:
        raise AssertionError('Не удалось ввести текст в поле')

@then('нажать на кнопку Поиск в google')
def step(context):
    context.page.click_gently(GooglePageLocators.SEARCH_BUTTON)

@then('найти ссылку "{url}"')
def step(context, url):
    context.page.find_link(url)

@then('нажать на ссылку "{url}"')
def step(context, url):
    context.page.go_to_selected_result(url)
    context.page = CBRPage(context.browser, context.browser.current_url)

@then('проверить, что открыт сайт Центрального банка РФ')
def step(context):
    assert context.page.check_url('http://www.cbr.ru/'), 'Открыт не тот сайт'

@then('нажать на кнопку Интернет-приемная')
def step(context):
    context.page.click_gently(CBRPageLocators.RECEPTION)

@then('открыть раздел Написать благодарность')
def step(context):
    context.page.click_gently(CBRPageLocators.GRATITUDE)

@then('ввести в поле Ваша благодарность значение "{text}"')
def step(context, text):
    try:
        field = context.browser.find_element(
                                *CBRPageLocators.GRATITUDE_MESSAGE)
        field.send_keys(text)
    except:
        raise AssertionError('Не удалось ввести текст в поле')

@then('поставить галочку Я согласен')
def step(context):
    context.page.click_gently(CBRPageLocators.AGREEMENT)

@then('сделать скриншот')
def step(context):
    try:
        path = (context.directory + "\screenshot" + 
                str(context.counter) + ".png")
        context.browser.save_screenshot(path)
        context.files.append(path)
        context.counter += 1
    except:
        raise AssertionError('Не удалось сохранить скриншот')

@then('нажать на кнопку Три полоски')
def step(context):
    context.page.click_gently(CBRPageLocators.BURGER)

@then('нажать на раздел О сайте')
def step(context):
    context.page.click_gently(CBRPageLocators.ABOUT)

@then('нажать на ссылку Предупреждение')
def step(context):
    context.page.click_gently(CBRPageLocators.WARNING)

@then('запомнить текст предупреждения')
def step(context):
    context.page.warning_text = context.page.warning_memory(
                                            CBRPageLocators.WARNING_TEXT)

@then('сменить язык страницы на EN')
def step(context):
    context.page.click_gently(CBRPageLocators.EN_LANG)

@then('проверить, что текст отличается от запомненного ранее')
def step(context):
    assert context.page.check_warning(
                CBRPageLocators.WARNING_TEXT), 'Текст не изменился'
