import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"]) # "GET" is done to retrieve site data, "POST" is done to send form data from website
def index():
    if request.method == "POST":

        name = request.form.get("name")
        try:
            month = int(request.form.get("month"))
            if month < 0 or month > 12:
                raise Exception
        except:
            return redirect("/")
        try:
            day = int(request.form.get("day"))
            if day < 0 or day > 31:
                raise Exception
        except:
            return redirect("/")

        if name.strip() != "" and month and day:
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", name, month, day)
            # In SQLite, since id INTEGER is PRIMARY KEY(id), it will auto-increment
            # However, if id should guarantee to be unique and sequential,
            # during CREATE TABLE birthdays, "id INTEGER NOT NULL AUTO_INCREMENT" should be used

        return redirect("/")

    else:

        results = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", results=results)


@app.route("/deleteEntry", methods=["GET"])
def deleteEntry():
    todelete = request.args.get("del")
    db.execute("DELETE FROM birthdays WHERE id = ?", todelete)

    return redirect("/")
