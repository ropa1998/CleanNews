import TrendRetriever
import NewsRetriever
from Utilities import getArgRegion, getBrowser_Firefox

browser = getBrowser_Firefox(invisible_window=False)

REGIONS = getArgRegion()

regions_with_trends = TrendRetriever.getTrends_Trends24(REGIONS, browser)
news = NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions_with_trends, browser)

browser.quit()
