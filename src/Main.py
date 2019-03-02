import TrendRetriever
import NewsRetriever
from Utilities import getArgRegion, getBrowser_Firefox, getAutomaticRegions

browser = getBrowser_Firefox(invisible_window=False)

REGIONS = getArgRegion()

regions_with_trends = TrendRetriever.getTrends_Trends24(REGIONS, browser)
regions_with_news = NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions_with_trends, browser)

for region in regions_with_news:
    print region.identifier
    for trend, article_list in region.get_news().items():
        print trend
        for article in article_list:
            print article.text

browser.quit()
