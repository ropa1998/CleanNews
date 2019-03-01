class Region:

    media = []
    identifier = ""
    trends = []
    useful_links = {}

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

    def addUsefulLink(self, link, trend):
        if trend in self.useful_links:
            self.useful_links[trend].append(link)
        else:
            new_list = [link]
            self.useful_links[trend] = new_list

    def get_news(self):
        return self.useful_links
