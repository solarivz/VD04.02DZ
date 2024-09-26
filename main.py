from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def films():
    return render_template("index.html")


@app.route("/index2/")
def person():
    return render_template("index2.html")


if __name__ == "__main__":
    app.run()