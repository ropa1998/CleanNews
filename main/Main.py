import TrendGetter
import TrendSearcher


browser = TrendSearcher.getBrowser_Firefox(invisible_window=False)
# LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
LOCATIONS = [""]
trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS, browser)
news = TrendSearcher.TrendSearch_Google(trends_per_region, browser)
browser.quit()
