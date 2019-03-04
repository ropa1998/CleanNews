from jinja2 import Template


def display_news(regions):
    t = Template("{%for region in regions%}"
                 "{{region.identifier}}"
                 "{%for trend in region.get_news()%}"
                 "{{trend}}"
                 "{% endfor %}"
                 "{% endfor %}")
    print t.render(regions=regions)

# for trend, article_list in region.get_news().items():
#     print trend
#     for article in article_list:
#         try:
#             print "-------"
#             print article.getTitle()
#             print article.getLink()
#             for text in article.body:
#                 print text
#             print "-------"
