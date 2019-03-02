import time

from selenium.webdriver.common.keys import Keys

from Article import Article


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
            query = "//article"
            matches = browser.find_elements_by_xpath(query)
            articles = []
            try:
                for match in matches:
                    article = Article(match.text, match.find_element_by_tag_name("a").get_attribute('href'))
                    articles.append(article)
            except:
                print
            for article in articles:
                for trend in region.getTrends():
                    if trend in article.title:
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
