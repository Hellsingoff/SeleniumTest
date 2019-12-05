import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from selenium import webdriver

def before_scenario(context, scenario):
    context.locator = {
        'en':'.header .langs > li:nth-child(2) > a',
        'ваша благодарность':'[name=MessageBody]',
        'интернет-приемная':'.header .important-links__item_ip > a',
        'написать благодарность':'.reception_type_container>div:nth-child(3)',
        'о сайте':'li.for_branch_11377 > a',
        'поиск':'[name=q]',
        'поиск в google':'[name=btnK]',
        'предупреждение':'[data-catalogid="11380"] > div > a',
        'сайт центрального банка рф':'www.cbr.ru',
        'текст предупреждения':'#content p',
        'три полоски':'.header .burger',
        'я согласен':'[type=checkbox]'
        }
    context.found = {}
    context.counter = 1
    context.directory = os.path.dirname(os.path.abspath(__file__))
    context.timer = 10
    context.files = []
    context.browser = webdriver.Chrome()
    context.browser.set_window_size(1024, 768)

def after_scenario(context, scenario):
    context.browser.quit()
    msg = MIMEMultipart()
    mail = 'hellsingoff@gmail.com'
    msg['From'] = mail
    msg['To'] = mail
    msg['Subject'] = 'test sreenshots'
    for file in context.files:
        with open(file, 'rb') as png:
            img = MIMEImage(png.read())
        msg.attach(img)
    '''Чтобы не публиковать пароль использован SMTP сервис Google,
    не требующий аутентификацию, но не поддерживающий шифрование.
    Из соображений безопасности письмо уходит в спам.'''
    smtp = smtplib.SMTP('aspmx.l.google.com', 25)
    smtp.sendmail(mail, mail, msg.as_string())
    smtp.close()
    for png in context.files:
        if os.path.isfile(png):
            os.remove(png)