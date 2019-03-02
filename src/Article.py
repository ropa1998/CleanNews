class Article:
    link = ""
    title = ""

    def __init__(self, title=title, link=link):
        self.link = link
        self.title = title

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link
