from flask import Flask, render_template, request
import requests
import json
from get_data import get_results
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        city = request.form['city']
        count, all_cities = get_results(city)
        return render_template("result.html", count=count, all_cities=all_cities)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
