from selenium import webdriver
import re


def cleanTrends(trends_per_region):
    """
    Takes all the trends an cleans them, meaning it takes away all hashtags and camelcase, to make better searches.
    :param trends_per_region: the map with the regions and the trends for each region
    :return: the same map, but clean (no hashtags or camelcase format)
    """
    # TODO optimize this algorithm
    # TODO solve for camel casing that is not actually camel casing. For example: BOCAxESPN, SCOvIRE
    for region in trends_per_region:
        cleanTrends = []
        removeTrends = []
        for trend in trends_per_region[region]:
            # takes hashtags away
            new_trend = trend.replace("#", '')
            # separates camelcase
            splitted = re.sub("(?!^)([A-Z][a-z]+)", r' \1', new_trend).split()
            new_trend = ''
            for elem in splitted:
                if len(new_trend) == 0:
                    new_trend = elem
                else:
                    new_trend = new_trend + " " + elem
            cleanTrends.append(new_trend)
            removeTrends.append(trend)
        for elem in removeTrends:
            trends_per_region[region].remove(elem)
        trends_per_region[region].extend(cleanTrends)

    return trends_per_region


def getTrends_Trends24(locations, browser):
    """
    This method returns a map with locations that reference a list
    of trends for that specific location. The site that is being used to get the information is
    trends24.in, which presents a list of trends for specific locations in Twitter.
    The method is specifically made for a websites because of its design. The same method
    cannot be used for other websites because not all pages share format.
    :param invisible_window: defines whether the window where the information will be
    retrieved from will be shown in the screen or not. Set originally in True. False should be used
    for debugging.
    :param locations: must be formatted to fit the standard for this page. It usually trends24.in/*country*/*region*
    :return: a map of locations:list of trends.
    """

    trends_url = "https://trends24.in/"
    trends_per_region = {}

    if not locations:
        return trends_per_region

    for location in locations:
        browser.get(trends_url + location)
        trend_card_list = browser.find_element_by_class_name("trend-card__list")
        trend_list = trend_card_list.find_elements_by_tag_name("li")
        trend_list_string = []
        for trend in trend_list:
            trend_list_string.append(trend.get_attribute("title"))
        trends_per_region[location] = trend_list_string

    trends_per_region = cleanTrends(trends_per_region)
    return trends_per_region



