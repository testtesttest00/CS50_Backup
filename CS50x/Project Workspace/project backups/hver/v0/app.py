import sqlite3
from flask import Flask, redirect, render_template, request, session


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("homepage.html", board=board, turn=0)


@app.route("/survey", methods=["GET", "POST"])
def survey():
    if request.method == "POST":
        try:
            c = int(request.form.get("cver"))
            p = int(request.form.get("pver"))
            h = int(request.form.get("hver"))
            long = request.form.get("long")
            for x in [c,p,h]:
                if x not in range(11):
                    raise Exception
        except:
            return render_template("failed.html")

        db_con = sqlite3.connect("database.db")
        db = db_con.cursor()
        db.execute("INSERT INTO survey (c, p, h, long)  VALUES (?, ?, ?, ?)", (c, p, h, long))
        db_con.commit()

        return redirect("/")

    else:
        return render_template("survey.html")
