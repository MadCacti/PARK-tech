from flask import Blueprint, render_template, request
from newsapi.newsapi_client import NewsApiClient
import requests

ratings = Blueprint('ratings', __name__,
                     url_prefix='/',
                     template_folder='templates',
                     static_folder='static', static_url_path='assets')

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


@ratings.route('/rating_test/')
def rating_test():
    total = len(onestar_list) + len(twostars_list) + len(threestars_list) + len(fourstars_list) + len(fivestars_list)
    sum = len(onestar_list) + len(twostars_list) * 2 + len(threestars_list) * 3 + len(fourstars_list) * 4 + len(fivestars_list) * 5
    if total != 0:
        average = sum / total
        average = round(average, 2)
    else:
        average = 0
    return render_template("ratings/rating_test.html", fivestarsreview=fivestars_list, fourstarsreview=fourstars_list, threestarsreview=threestars_list, twostarsreview=twostars_list, onestarreview=onestar_list, average=average)


@ratings.route('/fivestars', methods=['GET', 'POST'])
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


@ratings.route('/fourstars', methods=['GET', 'POST'])
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


@ratings.route('/threestars', methods=['GET', 'POST'])
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


@ratings.route('/twostars', methods=['GET', 'POST'])
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


@ratings.route('/onestar', methods=['GET', 'POST'])
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


@ratings.route('/info', methods=['GET', 'POST'])
def info():
    if request.form:
        resultA = request.form.get("input1")
        x = '{ "0":"Data A", "1":"Data B", "2":"Data C", "3":""}'
        # parse x:
        y = json.loads(x)
        myoutput = y[resultA]
        return render_template("ratings/rating_test.html", output=myoutput)
    return render_template("ratings/rating_test.html")


@ratings.route('/bookname', methods=['GET', 'POST'])
def bookname():
    if request.form:
        name = request.form.get("search")
        if len(name) != 0:
            return render_template("ratings/rating_test.html", rate="Rating for: ", thename=name)
    return render_template("ratings/rating_test.html")