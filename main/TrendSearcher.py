import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver


def TrendSearch_Google(trends_per_region, browser):

    for region in trends_per_region:
        for trend in trends_per_region[region]:
            browser.get('http://www.google.com')
            search = browser.find_element_by_name('q')
            search.send_keys(trend)
            search.send_keys(Keys.RETURN)
            time.sleep(5)


options = Options()
options.add_argument('--headless')


def getBrowser_Firefox(invisible_window):
    if invisible_window:
        return webdriver.Firefox(options=options)
    else:
        return webdriver.Firefox()