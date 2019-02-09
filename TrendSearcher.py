import time

from selenium.webdriver.common.keys import Keys


def TrendSearch_Google(trends_per_region, browser):

    for region in trends_per_region:
        for trend in trends_per_region[region]:
            browser.get('http://www.google.com')
            search = browser.find_element_by_name('q')
            search.send_keys(trend)
            search.send_keys(Keys.RETURN)
            time.sleep(5)