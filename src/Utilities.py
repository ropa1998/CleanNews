from Region import Region
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

options = Options()
options.add_argument('--headless')


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


def getArgRegion():
    arg_media = ["https://www.lanacion.com.ar/", "https://www.clarin.com/", "https://www.pagina12.com.ar/"]
    # arg_media = ["https://www.clarin.com/"]
    arg_identifier = "argentina"
    arg_region = Region(media=arg_media, identifier=arg_identifier)

    Regions = [arg_region]

    return Regions


def getBrowser_Firefox(invisible_window):
    if invisible_window:
        return webdriver.Firefox(options=options)
    else:
        return webdriver.Firefox()
