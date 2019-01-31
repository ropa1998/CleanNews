from selenium import webdriver


def getTrends_Trends24(locations):
    browser = webdriver.Firefox()
    trends_url = "https://trends24.in/"
    trends_per_region = {}

    for location in locations:
        browser.get(trends_url + location)
        trend_card_list = browser.find_element_by_class_name("trend-card__list")
        trend_list = trend_card_list.find_elements_by_tag_name("li")
        trend_list_string = []
        for trend in trend_list:
            trend_list_string.append(trend.get_attribute("title"))
        trends_per_region[location] = trend_list_string

    return trends_per_region

# LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
LOCATIONS = [""]

trends_per_region = getTrends_Trends24(LOCATIONS)
for elem in trends_per_region.get(""):
    print elem
