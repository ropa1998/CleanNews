from flask import Flask, render_template
import NewsRetriever
import TrendRetriever
from Utilities import getArgRegion, getBrowser_Firefox, print_regions, getAutomaticRegions

app = Flask(__name__)


@app.route('/')
def main_screen():
    # TODO add a way to choose which region you want analyzed.
    regions = process_regions()
    return render_template('layout.html', regions=regions)


def process_regions():
    browser = getBrowser_Firefox(invisible_window=False)
    regions = getAutomaticRegions()
    TrendRetriever.getTrends_Trends24(regions, browser)
    NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions, browser)
    print_regions(regions)
    NewsRetriever.BodyRetriever(regions, browser)
    print_regions(regions)

    browser.quit()

    return regions


if __name__ == '__main__':
    app.run(debug=True)
