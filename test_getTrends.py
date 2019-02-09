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
