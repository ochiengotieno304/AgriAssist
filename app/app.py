from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def view_home():
    return render_template("index.html", title="Home page")

@app.route("/first")
def view_first_page():
    return render_template("index.html", title="First page")

@app.route("/second")
def view_second_page():
    return render_template("index.html", title="Second page")