import time

from selenium.webdriver.common.keys import Keys


def TrendSearch_Google(regions, browser):
    for region in regions:
        for trend in region.getTrends():
            browser.get('http://www.google.com')
            search = browser.find_element_by_name('q')
            search.send_keys(trend)
            search.send_keys(Keys.RETURN)
            time.sleep(5)


def TrendSearchPerRegionThroughSpecificMedia(regions, browser):
    for region in regions:
        for medium in region.getMedia():
            browser.get(medium)
            scrollToTheBottom(browser)
            articles = browser.find_elements_by_tag_name('article')
            for article in articles:
                for trend in region.getTrends():
                    if trend in article.text:
                        region.addUsefulLink(article, trend)


def scrollToTheBottom(browser):
    lenOfPage = browser.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match = False
    while not match:
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = browser.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match = True
