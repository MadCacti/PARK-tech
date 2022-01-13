# import "packages" from flask
import json

# import app as app
import requests
from flask import Flask, render_template, request
from __init__ import app
from newsapi.newsapi_client import NewsApiClient

# from templates.crud.app_crud import app_crud

# app.register_blueprint(app_crud)

# create a Flask instance
app = Flask(__name__)

yourAPIKEY = '8169dc4f99474483ab5999bc2c761381'  # write your API key here
newsapi = NewsApiClient(api_key=yourAPIKEY)

# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/raiden/')
def raiden():
    return render_template("profiles/raiden.html", news='')


@app.route('/raiden/results/', methods=['POST'])
def get_results():
    keyword = request.form['keyword']  # getting input from user

    news = newsapi.get_top_headlines(q=keyword,
                                     # sources='bbc-news,the-verge',#optional and you can change
                                     # category='business', #optional and you can change also
                                     language='en',  # optional and you can change also
                                     country='in')
    # print(news['articles'])
    return render_template('profiles/raiden.html', news=news['articles'])

@app.route('/paul/')
def paul():
    return render_template("profiles/paul.html")


@app.route('/armaan/')
def armaan():
    return render_template("profiles/armaan.html")


@app.route('/TEST/')
def TEST():
    return render_template("profiles/TEST.html")


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
    print(output)
    return render_template("profiles/kurtis.html", question=output)
# runs the application on the development server
fivestars_list = []
fourstars_list = []
threestars_list = []
twostars_list = []
onestar_list = []


# def averagecalc():
#    average = 0
#    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
#    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
#    if total != 0:
#        average = sum / total


@app.route('/rating_test/')
def rating_test():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/fivestars', methods=['GET', 'POST'])
def fivestars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            fivestars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/fourstars', methods=['GET', 'POST'])
def fourstars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            fourstars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/threestars', methods=['GET', 'POST'])
def threestars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            threestars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/twostars', methods=['GET', 'POST'])
def twostars():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            twostars_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/onestar', methods=['GET', 'POST'])
def onestar():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    if request.form:
        review = request.form.get("review")
        if len(review) != 0:
            onestar_list.append(review)
            total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
            sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
            if total != 0:
                average = sum / total
                average = round(average, 2)
            else:
                average = 0
            return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@app.route('/databases/')
def databases():
    return render_template("Databases/databases.html")


@app.route('/search/')
def search():
    return render_template("search.html")


@app.route('/isbn/')
def isbn():
    return render_template("isbn.html")


@app.route('/database1/')
def database1():
    return render_template("Databases/database1.html")


@app.route('/moreinfo/')
def moreinfo():
    return render_template("moreinfo.html")


@app.route('/login/', methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route('/register/')
def register():
    return render_template("register.html")


@app.route('/error/')
def error():
    return render_template("error.html")


@app.route('/random')
def random():
    return render_template("randombook.html")
# @app.route('/crud')
# def crud():
#     """obtains all Users from table and loads Admin Form"""
#     return render_template("crud/templates/crud/crud.html")


if __name__ == "__main__":
    app.run(
        debug=True,
       # host="0.0.0.0",
       # port=5000
    ),