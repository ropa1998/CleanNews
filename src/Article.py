class Article:
    link = ""
    title = ""
    body = []

    def __init__(self, title=title, link=link):
        self.link = link
        self.title = title

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def setBody(self, body):
        self.body = body

    def __eq__(self, other):
        if other.title == self.title:
            return True
        return False

    def __hash__(self):
        return hash(self.title)
