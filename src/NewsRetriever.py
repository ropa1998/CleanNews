import time

from selenium.common.exceptions import TimeoutException, NoSuchAttributeException, NoSuchElementException, \
    WebDriverException
from selenium.webdriver.common.keys import Keys
import datetime

from Article import Article

# todo add documentation
# todo add README
from Utilities import monitor_prompt


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
            try:
                browser.get(medium)
                scrollToTheBottom(browser)
                print monitor_prompt("Reached the bottom of " + medium + ". ")
                query = "//article"
                matches = browser.find_elements_by_xpath(query)
                articles = []
            except TimeoutException:
                print "Timeout exception: site" + medium.link + "did not completely load after some time"
            except WebDriverException:
                print "Browser error. Skipping " + medium + "."
            try:
                for match in matches:
                    article = Article(match.text, match.find_element_by_tag_name("a").get_attribute('href'), medium)
                    articles.append(article)
            except NoSuchAttributeException:
                print "Not possible to create article from " + match.text + ". Missing attribute"
            except NoSuchElementException:
                print "Not possible to create article from " + match.text + ". Missing element"
            for article in articles:
                for trend in region.getTrends():
                    if trend in article.title:
                        region.addUsefulLink(article, trend)
            print monitor_prompt("Created articles for " + medium + ". ")
        region.cleanArticles()


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


def BodyRetriever(regions, browser):
    browser.set_page_load_timeout(60)
    for region in regions:
        for trend, article_list in region.get_news().items():
            for article in article_list:
                try:
                    browser.get(article.getLink())
                    paragraphs = browser.find_elements_by_tag_name("p")
                    full_text = ""
                    for paragraph in paragraphs:
                        if len(paragraph.text) > 100:
                            full_text = full_text + "\n" + paragraph.text
                        article.setBody(full_text)
                except TimeoutException:
                    print "Timeout exception: site " + article.link + "did not completely load in less than 60 seconds"

