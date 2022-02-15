# import "packages" from flask
import json

# import app as app
from flask import render_template, request
from __init__ import app
from crud.app_crud import app_crud
from blueprints.profiles import profiles
from blueprints.ratings import ratings
from frontend.frontend import app_frontend

app.register_blueprint(app_frontend)
app.register_blueprint(app_crud)
app.register_blueprint(profiles)
app.register_blueprint(ratings)
# create a Flask instance

# connects default URL to render index.html


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/databases/')
def databases():
    return render_template("Databases/databases.html")


@app.route('/search/')
def search():
    return render_template("search.html")

@app.route('/APct/')
def APct():
    return render_template("CreateTASK/APct.html")


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
    return render_template("usersystem/login.html")


@app.route('/register/')
def register():
    return render_template("usersystem/register.html")


@app.route('/timer/')
def timer():
    return render_template("timer.html")


@app.route('/bookstore/')
def bookstore():
    return render_template("bookstore.html")


@app.route('/randombook/')
def randombook():
    return render_template("randombook.html")


@app.route('/TEST/')
def TEST():
    return render_template("TEST.html")


@app.route('/error/')
def error():
    return render_template("usersystem/error.html")

@app.route('/random')
def random():
    return render_template("randombook.html")
# @app.route('/crud')
# def crud():
#     """obtains all Users from table and loads Admin Form"""
#     return render_template("crud/templates/crud/crud.html")
@app.route('/hangman/')
def hangman():
    return render_template("hangman.html")

@app.route('/wishlist1', methods=['GET', 'POST'])
def wishlist1(gen):
    if request.form:
        resultB = request.form.get("input1")
        booknames = []
        list1 = ["Harry Potter", "To kill a Mocking Bird", "Hunger Games", "The Great Gatsby", "The Giver"]
        list2 = ["Harry Potter", "To kill a Mocking Bird", "Hunger Games", "The Great Gatsby", "The Giver"]
        list3 = ["Harry Potter", "To kill a Mocking Bird", "Hunger Games", "The Great Gatsby", "The Giver"]
        mylist = list(gen)
        i = 0
        while i < len(mylist):
            print(f"Book {i + 1}")
            resultB = input("Would you like to add " + mylist[i] + " to your wishlist? ")
            if resultB == 'yes' or resultB == 'sure':
                booknames.append(mylist[i])
            i += 1
        return render_template("Databases/database1.html", theoutput=booknames)
    return render_template("Databases/database1.html")

@app.route('/wishlist2', methods=['GET', 'POST'])
def wishlist2():
    if request.form:
        resultA = request.form.get("input3")
        wishlist1(resultA)
        return render_template("Databases/database1.html")
    return render_template("Databases/database1.html")
if __name__ == "__main__":
    app.run( debug=True)