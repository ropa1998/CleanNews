from selenium import webdriver


def getTrends(locations):
    browser = webdriver.Firefox()
    trends_url = "https://trends24.in/"

    for location in locations:
        browser.get(trends_url + location)
        location_retrieved = browser.find_element_by_xpath('//*[@id="app-bar-toggle"]')
        location_retrieved_string = location_retrieved.get_attribute("title")
        print location_retrieved_string

        trend_card_list = browser.find_element_by_class_name("trend-card__list")
        trend_list = trend_card_list.find_elements_by_tag_name("li")
        for trend in trend_list:
            print trend.get_attribute("title")

        # trends = trend_list.find_element_by_tag_name("li")
        # for trend in trends:
        #     title = trend.get_attribute("title")
        #     print title

    # browser.get('http://seleniumhq.org/')


LOCATIONS = ["", "argentina", "argentina/buenos-aires"]

getTrends(LOCATIONS)
