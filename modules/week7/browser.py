from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep


def get_browser(url: str):
    profile = webdriver.FirefoxProfile()
    profile.set_preference(
        "general.useragent.override",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0",
    )
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options)
    browser.get(url)
    sleep(3)
    return browser
