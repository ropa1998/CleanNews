from flask import Flask, render_template

import NewsRetriever
import TrendRetriever
from Utilities import getArgRegion, getBrowser_Firefox, print_regions, monitor_prompt

app = Flask(__name__)

# todo improve design and architecture


@app.route('/')
def main_screen():
    try:
        # TODO add a way to choose which region you want analyzed.
        print monitor_prompt("Program Started. ")
        browser = getBrowser_Firefox(invisible_window=True)
        print monitor_prompt("Browser Started. ")
        regions = process_regions(browser)
        return render_template('layout.html', regions=regions, message="Welcome to your news digest")
    except:
        print "Process failed. Canceling operation"
        return render_template("layout.html", message="Something failed. Please try again later.")
    finally:
        browser.quit()


def process_regions(browser):
    regions = getArgRegion()
    TrendRetriever.getTrends_Trends24(regions, browser)
    print monitor_prompt("All trends for regions retrieved. ")
    NewsRetriever.TrendSearchPerRegionThroughSpecificMedia(regions, browser)
    print monitor_prompt("All news titles for regions retrieved. ")
    print_regions(regions)
    NewsRetriever.BodyRetriever(regions, browser)
    print monitor_prompt("All news bodies for regions retrieved. ")
    print_regions(regions)

    return regions


if __name__ == '__main__':
    app.run(debug=True)
