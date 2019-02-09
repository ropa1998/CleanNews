from unittest import TestCase
import TrendGetter

class TestGetTrends(TestCase):

    def test_getting_nonEmptyLocations(self):
        LOCATIONS = ["", "argentina", "argentina/buenos-aires"]
        # LOCATIONS = [""]

        trends_per_region = TrendGetter.getTrends_Trends24(LOCATIONS)

