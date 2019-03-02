from selenium.common.exceptions import NoSuchElementException

import TrendRetriever
import NewsRetriever
from Utilities import getArgRegion, getBrowser_Firefox, getAutomaticRegions

browser = getBrowser_Firefox(invisible_window=True)

regions = getArgRegion()

TrendRetriever.getTrends_Trends24(regions, browser)
NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions, browser)

for region in regions:
    print region.identifier
    for trend, article_list in region.get_news().items():
        print trend
        for article in article_list:
            try:
                print article.text
            except NoSuchElementException:
                print "An error ocurred."

browser.quit()
