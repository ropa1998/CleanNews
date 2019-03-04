from flask import Flask, render_template

import process

app = Flask(__name__)


@app.route('/')
def main_screen():
    # regions = process.main_process()
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)