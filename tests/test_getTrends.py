from unittest import TestCase
from main import TrendGetter
from main.TrendSearcher import getBrowser_Firefox


class TestGetTrends(TestCase):



    def test_getting_nonEmptyLocations(self):
        brw = getBrowser_Firefox(invisible_window=True)
        LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS,browser=brw)
        self.assertTrue(trends_per_region)
        self.assertTrue(len(trends_per_region) == 3)

    def test_gettingEmptyLocations(self):
        brw = getBrowser_Firefox(invisible_window=True)
        LOCATIONS = []
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS,browser=brw)
        self.assertFalse(trends_per_region)

    def test_visualization(self):
        brw = getBrowser_Firefox(invisible_window=True)
        LOCATIONS = [""]
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS,browser=brw)
        self.assertTrue(len(trends_per_region) == 1)

    def test_cleanHashtag(self):
        brw = getBrowser_Firefox(invisible_window=True)
        LOCATIONS = [""]
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS,browser=brw)
        trends_per_region = TrendGetter.cleanTrends(trends_per_region)
        for region in trends_per_region:
            for trend in trends_per_region[region]:
                self.assertFalse("#" in trend)
