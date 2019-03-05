from flask import Flask, render_template

import NewsRetriever
import TrendRetriever
from Utilities import getArgRegion, getBrowser_Firefox, print_regions, monitor_prompt

app = Flask(__name__)


@app.route('/')
def main_screen():
    attempts = 0
    ATTEMPT_LIMIT = 3
    while True:
        try:
            # TODO add a way to choose which region you want analyzed.
            print monitor_prompt("Program Started. ")
            browser = getBrowser_Firefox(invisible_window=True)
            print monitor_prompt("Browser opened.")
            regions = process_regions(browser)
            print monitor_prompt("Process finished. ")
            return render_template('layout.html', regions=regions, message="Welcome to your news digest")
        except:
            print "Process failed. Canceling operation"
            attempts = attempts + 1
            if attempts >= ATTEMPT_LIMIT:
                return render_template("layout.html", message="Something failed. The program tried running for "+ ATTEMPT_LIMIT + " times. Please try again later.")
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
