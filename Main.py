from selenium import webdriver
import TrendGetter
import TrendSearcher
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')


def getBrowser_Firefox(invisible_window):
    if invisible_window:
        return webdriver.Firefox(options=options)
    else:
        return webdriver.Firefox()


browser = getBrowser_Firefox(invisible_window=False)
# LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
LOCATIONS = [""]
trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS, browser)
news = TrendSearcher.TrendSearch_Google(trends_per_region, browser)
browser.quit()
