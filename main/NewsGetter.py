import re


def cleanTrends(trend):
    """
    Takes all the trends an cleans them, meaning it takes away all hashtags and camelcase, to make better searches.
    :param: trend: a string that is dirty. Has hashtag and camelcase
    :return: the same map, but clean (no hashtags or camelcase format)
    """
    # TODO optimize this algorithm
    # TODO solve for camel casing that is not actually camel casing. For example: BOCAxESPN, SCOvIRE
    if not trend:
        return trend

    # removes hashtags
    new_trend = trend.replace("#", '')
    # separates camelcase
    split = re.sub('(?!^)([A-Z][a-z]+)', r' \1', new_trend).split()
    new_trend = ''
    for elem in split:
        if len(new_trend) == 0:
            new_trend = elem
        else:
            new_trend = new_trend + " " + elem
    return new_trend


def getTrends_Trends24(regions, browser):
    """
    This method returns a list of regions with updated trends in for all regions. The site that is being used to get
    the information is trends24.in, which presents a list of trends for specific locations in Twitter. The method is
    specifically made for a websites because of its design. The same method cannot be used for other websites because
    not all pages share format. :param invisible_window: defines whether the window where the information will be
    retrieved from will be shown in the screen or not. Set originally in True. False should be used for debugging.

    :param browser: the browser of your choice for this search
    :param regions: a list of Region objects
    :return: regions with updated trends
    """

    trends_url = "https://trends24.in/"

    if not regions:
        return regions

    for region in regions:
        browser.get(trends_url + region.identifier)
        trend_card_list = browser.find_element_by_class_name("trend-card__list")
        trend_list = trend_card_list.find_elements_by_tag_name("li")
        trend_list_string = []
        for trend in trend_list:
            title = trend.get_attribute("title")
            clean_trend = cleanTrends(title)
            trend_list_string.append(clean_trend)
        region.changeTrends(trend_list_string)

    return regions
