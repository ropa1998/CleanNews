class Region:

    media = []
    identifier = ""
    trends = []
    useful_links = []

    def __init__(self, media=None, identifier=None):
        self.media = media
        self.identifier = identifier

    def getMedia(self):
        return self.media

    def getIdentifier(self):
        return self.identifier

    def updateTrends(self, trends):
        self.trends = trends

    def getTrends(self):
        return self.trends

    def addUsefulLink(self, link):
        self.useful_links.append(link)
