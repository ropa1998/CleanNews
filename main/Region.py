class Region:

    media = []
    identifier = ""
    trends = []

    def __init__(self, media=None, identifier=None):
        self.media = media
        self.identifier = identifier

    def getMedia(self):
        return self.media

    def getIdentifier(self):
        return self.identifier

    def addTrend(self, trend):
        self.trends.append(trend)

    def getTrends(self):
        return self.trends
