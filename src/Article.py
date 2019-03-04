class Article:
    link = ""
    title = ""
    body = ""
    medium = ""

    def __init__(self, title=title, link=link, medium = medium):
        self.link = link
        self.title = title
        self.medium = medium

    def getTitle(self):
        return self.title

    def getLink(self):
        return self.link

    def setBody(self, body):
        self.body = body

    def __eq__(self, other):
        if other.title == self.title or other.link == self.link:
            return True
        return False

    def __hash__(self):
        return hash(self.link+self.title)
