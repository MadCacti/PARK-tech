# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


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
def paul():
    return render_template("profiles/kurtis.html")
# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
