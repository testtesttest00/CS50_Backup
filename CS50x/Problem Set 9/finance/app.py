import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, unix

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd
app.jinja_env.filters["unix"] = unix

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_obj = db.execute("SELECT username, cash FROM users WHERE id = ?", session["user_id"])
    user = user_obj[0]["username"]
    cash = user_obj[0]["cash"]

    summary = get_holdings()

    return render_template("home.html", user=user, cash=cash, summary=summary)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").strip().upper()
        try:
            quantity = int(request.form.get("shares"))
            if quantity < 1:
                raise Exception
        except (ValueError, Exception):
            return apology("Invalid quantity")

        data_dict = lookup(symbol)
        try:
            price = float(data_dict["price"])
            cost = price * quantity
        except TypeError:
            return apology("Invalid query")

        cash_data = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = float(cash_data[0]["cash"])
        if cash < cost:
            return apology("Insufficient purchasing power")

        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash - cost, session["user_id"])
        db.execute("INSERT INTO transactions (user_id, symbol, direction, price, quantity, cost, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, "+", price, quantity, cost, os.times().elapsed
                   )

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?", session["user_id"])
    for transact in user_transactions:
        transact["time"] = transact["time"] + 1708886683 # Unix timestamp correction | possible numbers: 1708885496, 1708886683

    return render_template("history.html", data=user_transactions)


@app.route("/login", methods=["GET", "POST"]) # Dummy account: [username: Person] [password: a]
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    #Process search query
    if request.method == "POST":
        symbol = request.form.get("symbol").strip().upper()
        data_dict = lookup(symbol)
        try:
            data_dict["name"]
            return render_template("quote.html", symbol=symbol, dict=data_dict)
        except TypeError:
            return apology("Invalid query")

    else:
        return render_template("quote.html", symbol=0)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    #Process form data
    if request.method == "POST":
        name = request.form.get("username").strip()
        pass1 = request.form.get("password").strip()
        pass2 = request.form.get("confirmation").strip()

        # Error case: Empty username field
        if name == "":
            return apology("Invalid username")
        # Error case: Empty password field
        if pass1 == "":
            return apology("Invalid password")
        # Error case: Password confirmation fails
        if pass1 != pass2:
            return apology("Passwords do not match")

        try:
            db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", name, generate_password_hash(pass1))
            return render_template("register.html", value="success")
        # Error case: Insertion of duplicate username
        except ValueError:
            return apology("Username already exists")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    holdings = get_holdings()

    if request.method == "POST":
        try:
            symbol = request.form.get("symbol").strip()
            if symbol == "":
                raise Exception
        except (TypeError, Exception):
            return apology("Invalid query")

        quantity = int(request.form.get("shares"))
        if quantity < 1:
            return apology("Invalid quantity")

        if symbol not in holdings or holdings[symbol]["quantity"] < quantity:
            return apology("Insufficient shares")

        price = lookup(symbol)["price"]
        revenue = quantity * price
        user_obj = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        cash = user_obj[0]["cash"]

        db.execute("INSERT INTO transactions (user_id, symbol, direction, price, quantity, cost, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   session["user_id"], symbol, "-", price, quantity, -revenue, os.times().elapsed
                   )
        db.execute("UPDATE users SET cash = ? WHERE id = ?", cash + revenue, session["user_id"])

        return redirect("/")

    else:
        options = list(holdings)
        return render_template("sell.html", options=options)


def get_holdings():
    user_transactions = db.execute(
        "SELECT symbol, SUM(quantity) AS quantity, direction, time FROM transactions WHERE user_id = ? GROUP BY symbol, direction",
        session["user_id"]
        )
    summary = {}
    for transact in user_transactions:
        symbol = transact["symbol"]
        quantity = int(transact["direction"]+str(transact["quantity"]))
        try:
            total = summary[symbol]["quantity"]
            total = total + quantity
            summary[symbol]["quantity"] = total
            price = lookup(symbol)["price"]
            summary[symbol]["price"] = price
            total = summary[symbol]["total"]
            total = total + quantity*price
            summary[symbol]["total"] = total
        except KeyError:
            price = lookup(symbol)["price"]
            summary[symbol] = {"quantity":quantity, "price":price, "total":quantity*price}

        for symbol in list(summary):
            if summary[symbol]["quantity"] == 0:
                summary.pop(symbol)

    return summary
