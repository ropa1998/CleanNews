import NewsGetter
import TrendSearcher
from main.Region import Region


def getAutomaticRegions():
    arg_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    arg_identifier = "argentina"
    arg_region = Region(media=arg_media, identifier=arg_identifier)

    world_media = ["https://www.aljazeera.com/", "https://www.nytimes.com/", "https://www.bbc.com/"]
    world_identifier = ""
    world_region = Region(media=world_media, identifier=world_identifier)

    buenos_aires_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    buenos_aires_identifier = "argentina/buenos-aires"
    buenos_aires_region = Region(media=buenos_aires_media, identifier=buenos_aires_identifier)

    Regions = [arg_region, world_region, buenos_aires_region]

    return Regions


browser = TrendSearcher.getBrowser_Firefox(invisible_window=False)

REGIONS = getAutomaticRegions()

regions_with_trends = NewsGetter.getTrends_Trends24(REGIONS, browser)

# for region in regions_with_trends:
#     print "--------------"
#     print region.identifier
#     print region.getTrends()

news = TrendSearcher.TrendSearch_Google(regions_with_trends, browser)


browser.quit()
