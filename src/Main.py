import TrendRetriever
import NewsRetriever
from Utilities import getAutomaticRegions, getBrowser_Firefox

browser = getBrowser_Firefox(invisible_window=False)

REGIONS = getAutomaticRegions()

regions_with_trends = TrendRetriever.getTrends_Trends24(REGIONS, browser)
news = NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions_with_trends, browser)



browser.quit()
