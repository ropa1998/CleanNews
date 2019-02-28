from unittest import TestCase

import TrendRetriever
from Utilities import getBrowser_Firefox, getAutomaticRegions


class TestGetTrends(TestCase):

    brw = getBrowser_Firefox(invisible_window=True)

    def test_getting_nonEmptyLocations(self):
        REGIONS = getAutomaticRegions()
        regions = TrendRetriever.getTrends_Trends24(REGIONS, browser=self.brw)
        self.assertTrue(regions)
        self.assertTrue(len(regions) == 3)

    def test_gettingEmptyLocations(self):
        REGIONS = []
        regions = TrendRetriever.getTrends_Trends24(REGIONS, browser=self.brw)
        for region in regions:
            self.assertFalse(region.getTrends())

    def test_cleanHashtag(self):
        REGIONS = getAutomaticRegions()
        regions = TrendRetriever.getTrends_Trends24(REGIONS, browser=self.brw)
        for region in regions:
            for trend in region.getTrends():
                self.assertFalse("#" in trend)
