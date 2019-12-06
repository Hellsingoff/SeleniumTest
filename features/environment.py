import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from selenium import webdriver

def before_scenario(context, scenario):
    context.counter = 1
    context.directory = os.path.dirname(os.path.abspath(__file__))
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
    try:
        for file in context.files:
            with open(file, 'rb') as png:
                img = MIMEImage(png.read())
            msg.attach(img)
    except OSError:
        raise AssertionError("Ошибка при добавлении скриншота к письму")
    '''Чтобы не публиковать пароль использован SMTP сервис Google,
    не требующий аутентификацию, но не поддерживающий шифрование.
    Из соображений безопасности письмо уходит в спам.'''
    try:
        smtp = smtplib.SMTP('aspmx.l.google.com', 25)
        smtp.sendmail(mail, mail, msg.as_string())
        smtp.close()
    except:
        raise AssertionError("Ошибка при отправке письма")
    finally:
        try:
            for png in context.files:
                if os.path.isfile(png):
                    os.remove(png)
        except OSError:
            raise AssertionError("Ошибка при удалении скриншотов")