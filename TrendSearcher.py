import time

from selenium.webdriver.common.keys import Keys
from TrendGetter import getBrowser_Firefox


def TrendSearch_Google(trends_per_region, invisible_window = True):

    browser = getBrowser_Firefox(invisible_window=invisible_window)

    for region in trends_per_region:
        for trend in trends_per_region[region]:
            browser.get('http://www.google.com')
            search = browser.find_element_by_name('q')
            search.send_keys(trend)
            search.send_keys(Keys.RETURN)
            time.sleep(5)

    browser.quit()