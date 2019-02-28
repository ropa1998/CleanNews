from unittest import TestCase
from main import NewsGetter
from main.Region import Region
from main.TrendSearcher import getBrowser_Firefox
import test_region


class TestGetTrends(TestCase):

    brw = getBrowser_Firefox(invisible_window=True)

    arg_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    arg_identifier = "argentina"
    arg_region = Region(media=arg_media, identifier=arg_identifier)

    world_media = ["https://www.aljazeera.com/", "https://www.nytimes.com/", "https://www.bbc.com/"]
    world_identifier = ""
    world_region = Region(media=world_media, identifier=world_identifier)

    buenos_aires_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    buenos_aires_identifier = "argentina/buenos-aires"
    buenos_aires_region = Region(media=buenos_aires_media, identifier=buenos_aires_identifier)

    def test_getting_nonEmptyLocations(self):
        REGIONS = [self.arg_region,self.world_region,self.buenos_aires_region]
        regions = NewsGetter.getTrends_Trends24(REGIONS, browser=self.brw)
        self.assertTrue(regions)
        self.assertTrue(len(regions) == 3)

    def test_gettingEmptyLocations(self):
        REGIONS = []
        regions = NewsGetter.getTrends_Trends24(REGIONS, browser=self.brw)
        for region in regions:
            self.assertFalse(region.getTrends())

    def test_visualization(self):
        REGIONS = [self.arg_region]
        regions = NewsGetter.getTrends_Trends24(REGIONS, browser=self.brw)
        self.assertTrue(len(regions) == 1)

    def test_cleanHashtag(self):
        REGIONS = [self.arg_region,self.world_region,self.buenos_aires_region]
        regions = NewsGetter.getTrends_Trends24(REGIONS, browser=self.brw)
        for region in regions:
            for trend in region.getTrends():
                self.assertFalse("#" in trend)
