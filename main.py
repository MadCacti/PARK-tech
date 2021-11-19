# import "packages" from flask
import json

from flask import Flask, render_template, request
# from newsapi.newsapi_client import NewsApiClient
import requests
# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/raiden/')
def raiden():
    return render_template("profiles/raiden.html")


@app.route('/paul/')
def paul():
    return render_template("profiles/paul.html")


@app.route('/armaan/')
def armaan():
    return render_template("profiles/armaan.html")


@app.route('/kurtis/')
def kurtis():

    url = "https://trivia-by-api-ninjas.p.rapidapi.com/v1/trivia"
    querystring = {"category":"sciencenature","limit":"1"}
    headers = {
        'x-rapidapi-host': "trivia-by-api-ninjas.p.rapidapi.com",
        'x-rapidapi-key': "6279ac9b7amsh7dc015c7d7746fbp1f4d65jsn125b0c500438"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    output = json.loads(response.text)
    return render_template("profiles/kurtis.html", question=output)
# runs the application on the development server


if __name__ == "__main__":
    app.run(debug=True)
