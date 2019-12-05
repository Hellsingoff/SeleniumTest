import behave
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('открыт сайт "{url}"')
def step(context, url):
    context.browser.get('http:\\' + url)

@then('проверить, что появилось поле "{field}"')
def step(context, field):
    field = field.lower()
    wait = EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, context.locator[field]))
    WebDriverWait(context.browser, context.timer).until(wait)

@then('ввести в поле "{field}" значение "{text}"')
def step(context, field, text):
    field = field.lower()
    if field in context.locator:
        field_element = context.browser.find_element_by_css_selector(
                                                context.locator[field])
        field_element.send_keys(text)

@then('нажать на "{obj_name}"')
def step(context, obj_name):
    obj_name = obj_name.lower()
    if obj_name in context.locator:
        waiting = EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, context.locator[obj_name]))
        WebDriverWait(context.browser, context.timer).until(waiting).click()
    elif obj_name in context.found:
        context.found[obj_name].click()
        # На случай открытия новой страницы в новой вкладке:
        context.browser.switch_to_window(context.browser.window_handles[-1])
        

@then('найти ссылку "{url}"')
def step(context, url):
    context.found[url.lower()] = (
            context.browser.find_element_by_css_selector(
                                            '[href$="%s/"]' % url.lower()))

@then('проверить, что открыт "{site}"')
def step(context, site):
    site = context.locator[site.lower()]
    opened_url = context.browser.current_url
    assert (opened_url == "http://" + site + "/" or 
            opened_url == "https://" + site + "/")

@then('поставить галочку "{check}"')
def step(context, check):
    context.execute_steps('Тогда нажать на "%s"' % check)

@then('сделать скриншот')
def step(context):
    path = context.directory + "\screenshot" + str(context.counter) + ".png"
    context.browser.save_screenshot(path)
    context.files.append(path)
    context.counter += 1

@then('запомнить "{obj}"')
def step(context, obj):
    obj = obj.lower()
    to_mem = obj + '_remembered'
    context.locator[to_mem] = context.browser.find_element_by_css_selector(
                                                context.locator[obj]).text

@then('сменить язык на "{lang}"')
def step(context, lang):
    context.execute_steps('Тогда нажать на "%s"' % lang)

@then('проверить, что "{obj}" изменился')
def step(context, obj):
    obj = obj.lower()
    from_mem = obj + '_remembered'
    assert (context.locator[from_mem] != 
            context.browser.find_element_by_css_selector(
                    context.locator[obj]).text), "%s не изменился!" % obj
