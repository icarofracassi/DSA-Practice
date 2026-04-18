import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

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
    values = db.execute("SELECT symbol, SUM(value) AS total_value, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
    for row in values:
        currentvalue = lookup(row.get('symbol'))
        row['current_value'] = currentvalue.get("price")*int(row.get('total_shares'))

    currentCash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    currentCash = currentCash[0].get("cash")

    return render_template("index.html", values=values, currentCash=currentCash)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")


    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology("Non numeric number of shares")
        if shares <= 0:
            return apology("Non positive number of shares")

        try:
            values = lookup(symbol)
            if values is None:
                return apology("Quote returned Null, please change symbol.")

            stockCurrentValue = values.get("price")
            transactionTotalCost = stockCurrentValue * shares

            currentCash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
            currentCash = currentCash[0].get("cash")
            print("currentCash: ", currentCash)

            if currentCash < transactionTotalCost:
                return apology("Not enough cash")

            print("shares:" , shares)

            newcashvalue = currentCash - transactionTotalCost
            db.execute("INSERT INTO transactions (user_id, value, shares, symbol) VALUES(?, ?, ?, ?)", session["user_id"], transactionTotalCost, shares, symbol)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", newcashvalue, session["user_id"])

            return redirect("/")
        except ValueError:
            return apology(ValueError)

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    values = db.execute("SELECT * FROM transactions WHERE user_id = ? ORDER BY timestamp DESC", session["user_id"])
    return render_template("history.html", values=values)

@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    """Show cart for adding cash"""
    if request.method == "GET":
        return render_template("cart.html")

    else:
        valuecart = request.form.get("amount")
        try:
            valuecart = int(valuecart)
        except ValueError:
            return apology("Invalid amount format")

        if valuecart < 0:
            return apology("Invalid amount")


        currentCash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        currentCash = currentCash[0].get("cash")
        newcashvalue = currentCash + valuecart

        db.execute("UPDATE users SET cash = ? WHERE id = ?", newcashvalue, session["user_id"])
        return redirect("/")



@app.route("/login", methods=["GET", "POST"])
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
    if request.method == "GET":
        return render_template("quote.html")

    else:
        symbol = request.form.get("symbol")

        try:
            values = lookup(symbol)
            print("values: ", values)
            if values is None:
                return apology("Quote returned Null, please change symbol.")
            print("symbol: ", symbol)
            return render_template("quoted.html", values=values, symbol=symbol)
        except ValueError:
            return apology(ValueError)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    else:
        # Access form data
        username = request.form.get("username")
        if not username:
            return apology("No Username")

        password = request.form.get("password")
        if not password:
            return apology("No password")

        confirmation = request.form.get("confirmation")
        if not confirmation:
            return apology("No confirmation")

        if password != confirmation:
            return apology("Confirmation does not match password")

        hashpass = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashpass)
            return redirect("/")

        except ValueError:
            return apology("Username already exists")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    if request.method == "GET":
        values = db.execute("SELECT symbol FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        return render_template("sell.html", values=values)
    else:
        values = db.execute("SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        availablesymbols = []
        shares = request.form.get("shares")
        try:
            shares = int(shares)
        except ValueError:
            return apology ("Shares not a number")

        symbol = request.form.get("symbol")

        for row in values:
            availablesymbols.append(row.get('symbol'))
            if row.get('symbol') == symbol:
                if shares > row.get('total_shares'):
                    return apology("No such stocks for that symbol")

        if symbol not in availablesymbols:
            return apology("No stock for that symbol")


        lookupvalues = lookup(symbol)
        stockCurrentValue = lookupvalues.get("price")
        transactionTotalValue = stockCurrentValue * shares

        currentCash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        currentCash = currentCash[0].get("cash")
        newcashvalue = currentCash + transactionTotalValue
        negativeshares = shares*-1

        db.execute("INSERT INTO transactions (user_id, value, shares, symbol) VALUES(?, ?, ?, ?)", session["user_id"], transactionTotalValue, negativeshares, symbol)
        db.execute("UPDATE users SET cash = ? WHERE id = ?", newcashvalue, session["user_id"])
        return redirect("/")
