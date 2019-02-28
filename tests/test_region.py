from unittest import TestCase

from main.Region import Region


class TestRegion(TestCase):

    arg_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    arg_identifier = "argentina"
    arg_region = Region(media=arg_media, identifier=arg_identifier)

    world_media = ["https://www.aljazeera.com/","https://www.nytimes.com/","https://www.bbc.com/"]
    world_identifier = ""
    world_region = Region(media=world_media, identifier=world_identifier)

    buenos_aires_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    buenos_aires_identifier = "argentina/buenos-aires"
    buenos_aires_region = Region(media=buenos_aires_media, identifier=buenos_aires_identifier)

    def arg_region(self):
        return self.arg_region

    def test_init(self):
        self.assertTrue(self.arg_region.getMedia(), self.arg_media)
        self.assertTrue(self.arg_region.getIdentifier(), self.arg_identifier)
