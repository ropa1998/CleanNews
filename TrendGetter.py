from selenium import webdriver


def getTrends_Trends24(locations):
    """
    This method returns a map with locations that reference a list
    of trends for that specific location. The site that is being used to get the information is
    trends24.in, which presents a list of trends for specific locations in Twitter.
    :param locations: must be formatted to fit the standard for this page. It usually trends24.in/*country*/*region*
    :return: a map of locations:list of trends.
    """
    from selenium.webdriver.firefox.options import Options

    options = Options()
    options.add_argument('--headless')

    browser = webdriver.Firefox(options=options)
    trends_url = "https://trends24.in/"
    trends_per_region = {}

    if(locations == False):
        return trends_per_region

    for location in locations:
        browser.get(trends_url + location)
        trend_card_list = browser.find_element_by_class_name("trend-card__list")
        trend_list = trend_card_list.find_elements_by_tag_name("li")
        trend_list_string = []
        for trend in trend_list:
            trend_list_string.append(trend.get_attribute("title"))
        trends_per_region[location] = trend_list_string

    return trends_per_region
