import time
import behave
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:
    lct = {
        'поиск':'[name=q]',
        'сайт центрального банка рф':'www.cbr.ru',
        'ваша благодарность':'[name=MessageBody]',
        'написать благодарность':'.reception_type_container>div:nth-child(3)',
        'поиск в google':'[name=btnK]',
        'интернет-приемная':'.header > .important-links__item_ip > a',
        'три полоски':'.header .burger',
        'о сайте':'li.for_branch_11377 > a',
        'предупреждение':'[data-catalogid="11380"] > div > a',
        'en':'.header .langs > li:nth-child(2) > a'
        }
    finded = {}
    cntr = 1

@given('открыт сайт "{url}"')
def step(cont, url):
    cont.browser = webdriver.Chrome()
    cont.browser.set_window_size(1024, 768)
    cont.browser.get('http:\\' + url)

@then('проверить, что появилось поле "{field}"')
def step(cont, field):
    field = field.lower()
    WebDriverWait(cont.browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, Locators.lct[field]))
    )

@then('ввести в поле "{field}" значение "{text}"')
def step(cont, field, text):
    field = field.lower()
    if field in Locators.lct:
        fd_el = cont.browser.find_element_by_css_selector(Locators.lct[field])
        fd_el.send_keys(text)

@then('нажать на "{obj_name}"')
def step(cont, obj_name):
    obj_name = obj_name.lower()
    if obj_name in Locators.lct:
        WebDriverWait(cont.browser, 10).until(EC.element_to_be_clickable((
                                    By.CSS_SELECTOR, Locators.lct[obj_name]))
        ).click()
    elif obj_name in Locators.finded:
        Locators.finded[obj_name].click()
        cont.browser.switch_to_window(cont.browser.window_handles[-1])
        

@then('найти ссылку "{url}"')
def step(cont, url):
    Locators.finded[url.lower()] = cont.browser.find_element_by_css_selector(
                          '[href$="%s/"]' % url
                          )

@then('проверить, что открыт "{site}"')
def step(cont, site):
    site = Locators.lct[site.lower()]
    cur_url = cont.browser.current_url
    assert (cur_url == "http://" + site + "/" or 
            cur_url == "https://" + site + "/"
            )

@then('поставить галочку "{check}"')
def step(cont, check):
    cont.browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()

@then('сделать скриншот')
def step(cont):
    cont.browser.save_screenshot("screenshot" + str(Locators.cntr) + ".png")
    Locators.cntr += 1

@then('запомнить текст предупреждения')
def step(cont):
    Locators.lct['remembered'] = cont.browser.find_element(
                            By.CSS_SELECTOR, '#content p').text

@then('сменить язык на "{lang}"')
def step(cont, lang):
    cont.execute_steps('Тогда нажать на "%s"' % lang)

@then('проверить, что текст изменился')
def step(cont):
    assert Locators.lct['remembered'] != cont.browser.find_element(
                            By.CSS_SELECTOR, '#content p').text
