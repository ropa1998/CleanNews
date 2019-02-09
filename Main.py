import TrendGetter
import TrendSearcher

LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS, invisible_window=True)
news = TrendSearcher.TrendSearch_Google(trends_per_region, invisible_window=False)
