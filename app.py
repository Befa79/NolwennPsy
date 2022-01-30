import os
from flask import (Flask, render_template, redirect, url_for)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


@app.route("/")
def getindex():
    return render_template("index.html")


@app.route("/gettest")
def gettest():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
