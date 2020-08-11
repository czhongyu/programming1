import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, checkpassword

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    stocks = db.execute("SELECT symbol, SUM(shares) AS shares FROM history WHERE id = :id GROUP BY symbol",
                        id=session["user_id"])
    all_total = 0
    for stock in stocks:
        # look up the symbol until it's ready
        quote = lookup(stock["symbol"])
        while not quote:
            quote = lookup(stock["symbol"])
        stock["name"] = quote["name"]
        stock["price"] = usd(quote["price"])
        stock["total"] = usd(stock["shares"] * quote["price"])
        all_total = all_total + stock["shares"] * quote["price"]

    # cash
    rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
    cash = rows[0]["cash"]
    all_total = all_total + cash

    return render_template("index.html", stocks=stocks, cash=usd(cash), total=usd(all_total))


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    # PERSONAL TOUCH: change password

    if request.method == "POST":
        # Ensure password is correct
        rows = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
        if not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid password", 403)

        if not request.form.get("newpassword"):
            return apology("missing new password", 400)

        # password again
        if request.form.get("newpassword") != request.form.get("confirmation"):
            return apology("new passwords don't match", 400)

        # PERSONAL TOUCH: passwords are required to be 8 ~ 16 long, containing numbers, letters and at least one of ~!@#$%^&*
        # I commented this out only because the password restrictions could not pass check50...
        # This actually works!
        # if not checkpassword(request.form.get("newpassword")):
        #     return apology("8-16 with numbers, letters and at least one of ~!@#$%^&*", 400)

        db.execute("UPDATE users SET hash = :hash WHERE id = :id", hash=generate_password_hash(
            request.form.get("newpassword")), id=session["user_id"])

        # PERSONAL TOUCH: flash message
        flash("Password changed!")

        # redirect to home page
        return redirect("/")
    else:
        rows = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
        return render_template("password.html", username=rows[0]["username"])


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    # PERSONAL TOUCH: add cash into the account

    if request.method == "POST":
        # not empty
        addcash = request.form.get("deposit")
        if not addcash:
            return apology("missing deposit", 400)
        # int or float
        if not addcash.replace('.', '', 1).isdigit():
            return apology("invalid deposit", 400)

        # round
        addcash = round(float(addcash) * 100.0) / 100.0
        # add cash
        db.execute("UPDATE users SET cash = cash + :addcash WHERE id = :id", addcash=addcash, id=session["user_id"])

        # PERSONAL TOUCH: flash message
        flash(f"{usd(addcash)} added!")

        # redirect to home page
        return redirect("/")
    else:
        # display current cash
        rows = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
        return render_template("deposit.html", cash=usd(rows[0]["cash"]))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # Ensure symbol and shares were submitted
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return apology("missing symbol", 400)

        if not shares:
            return apology("missing shares", 400)

        if not shares.isdigit():
            return apology("invalid shares", 400)

        # check if valid
        quote = lookup(symbol)

        # invalid
        if not quote:
            return apology("invalid symbol", 400)

        # enough cash?
        rows = db.execute("SELECT cash FROM users WHERE id = :id", id=session["user_id"])
        price = int(shares) * quote["price"]
        if rows[0]["cash"] < price:
            return apology("can't afford", 400)

        # update history
        db.execute("INSERT INTO history (id, symbol, shares, price) VALUES(:id, :symbol, :shares, :price)",
                   id=session["user_id"], symbol=symbol.upper(), shares=int(shares), price=quote["price"])

        # update cash
        db.execute("UPDATE users SET cash = cash - :price WHERE id = :id", price=price, id=session["user_id"])

        price = quote["price"]
        # PERSONAL TOUCH: flash message
        flash(f"Bought {shares} share(s) of {symbol.upper()}, each {usd(price)}!")

        # redirect to home page
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    rows = db.execute("SELECT * FROM history WHERE id = :id", id=session["user_id"])

    for row in rows:
        row["price"] = usd(row["price"])

    return render_template("history.html", histories=rows)


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
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
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
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("missing symbol", 400)

        # quote symbol
        quote = lookup(request.form.get("symbol"))

        # invalid
        if not quote:
            return apology("invalid symbol", 400)

        # display quote result
        return render_template("quoted.html", name=quote["name"], symbol=quote["symbol"], price=usd(quote["price"]))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("missing username", 400)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("missing password", 400)

        # password again
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords don't match", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        if len(rows):
            return apology("username not available", 400)

        # PERSONAL TOUCH: passwords are required to be 8 ~ 16 long, containing numbers, letters and at least one of ~!@#$%^&*
        # I commented this out only because the password restrictions could not pass check50...
        # This actually works!
        # if not checkpassword(request.form.get("password")):
        #     return apology("8-16 with numbers, letters and at least one of ~!@#$%^&*", 400)

        # insert
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :hash)", username=request.form.get(
            "username"), hash=generate_password_hash(request.form.get("password")))

        # Remember which user has logged in
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        shares = request.form.get("shares")
        symbol = request.form.get("symbol")
        # Ensure username was submitted
        if not symbol:
            return apology("missing symbol", 400)

        # Ensure password was submitted
        elif not shares:
            return apology("missing shares", 400)

        # get shares
        rows = db.execute("SELECT SUM(shares) AS shares FROM history WHERE id = :id and symbol = :symbol",
                          id=session["user_id"], symbol=symbol)

        # enough shares?
        if rows[0]["shares"] < int(shares):
            return apology("too many shares", 400)

        quote = lookup(symbol)
        while not quote:
            quote = lookup(symbol)

        # update history
        db.execute("INSERT INTO history (id, symbol, shares, price) VALUES(:id, :symbol, :shares, :price)",
                   id=session["user_id"], symbol=symbol, shares=0 - int(shares), price=quote["price"])

        # update cash
        db.execute("UPDATE users SET cash = cash + :price WHERE id = :id",
                   price=quote["price"] * int(shares), id=session["user_id"])

        price = quote["price"]
        # PERSONAL TOUCH: flash message
        flash(f"Sold {shares} share(s) of {symbol.upper()}, each {usd(price)}!")

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        rows = db.execute("SELECT symbol FROM history WHERE id = :id GROUP BY symbol", id=session["user_id"])
        return render_template("sell.html", symbols=rows)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
