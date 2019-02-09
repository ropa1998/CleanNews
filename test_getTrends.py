from unittest import TestCase
import TrendGetter


class TestGetTrends(TestCase):

    def test_getting_nonEmptyLocations(self):
        LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS)
        self.assertTrue(trends_per_region)
        self.assertTrue(len(trends_per_region) == 3)

    def test_gettingEmptyLocations(self):
        LOCATIONS = []
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS)
        self.assertFalse(trends_per_region)

    def test_visualization(self):
        LOCATIONS = [""]
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS, invisible_window=False)
        self.assertTrue(len(trends_per_region) == 1)

    def test_cleanHashtag(self):
        LOCATIONS = [""]
        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS, invisible_window=False)
        trends_per_region = TrendGetter.cleanHashtags(trends_per_region)
        for region in trends_per_region:
            for trend in trends_per_region[region]:
                self.assertFalse("#" in trend)
