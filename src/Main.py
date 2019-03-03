import NewsDisplayer
import NewsRetriever
import TrendRetriever
from Utilities import getArgRegion, getBrowser_Firefox, print_regions

browser = getBrowser_Firefox(invisible_window=False)


regions = getArgRegion()

TrendRetriever.getTrends_Trends24(regions, browser)
# NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions, browser)
# # print_regions(regions)
# NewsRetriever.BodyRetriever(regions, browser)
# # print_regions(regions)
NewsDisplayer.display_news(regions)



browser.quit()
