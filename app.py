import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helper import login_required, apology

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


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///blog.db")


db.execute("CREATE TABLE IF NOT EXISTS 'users' ('id' INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 'nickname' TEXT NOT NULL, 'username' TEXT NOT NULL, 'hash' TEXT NOT NULL)")
# Creating comment table for each post
db.execute("CREATE TABLE IF NOT EXISTS 'thumb1' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb2' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb3' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb4' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb5' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb6' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb7' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb8' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb9' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'comment' TEXT NOT NULL)")

# Creating like table for each post
db.execute("CREATE TABLE IF NOT EXISTS 'thumb1 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb2 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb3 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb4 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb5 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb6 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb7 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb8 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")
db.execute("CREATE TABLE IF NOT EXISTS 'thumb9 likes' ('id' INTEGER NOT NULL, 'nickname' TEXT NOT NULL, 'likes' INTEGER)")


db.execute("CREATE TABLE IF NOT EXISTS 'all_comments_likes' ('name' TEXT, 'comments' INTEGER, 'likes' INTEGER)")
total_comments = db.execute("SELECT * FROM all_comments_likes")
if len(total_comments) == 0:
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('total', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb1', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb2', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb3', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb4', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb5', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb6', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb7', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb8', '0', '0')")
    db.execute("INSERT INTO all_comments_likes (name, comments, likes) VALUES ('thumb9', '0', '0')")

thumb1_comment_update = db.execute("SELECT * FROM thumb1")

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    # Update comments
    thumb1_comment_update = db.execute("SELECT * FROM thumb1")
    thumb2_comment_update = db.execute("SELECT * FROM thumb2")
    thumb3_comment_update = db.execute("SELECT * FROM thumb3")
    thumb4_comment_update = db.execute("SELECT * FROM thumb4")
    thumb5_comment_update = db.execute("SELECT * FROM thumb5")
    thumb6_comment_update = db.execute("SELECT * FROM thumb6")
    thumb7_comment_update = db.execute("SELECT * FROM thumb7")
    thumb8_comment_update = db.execute("SELECT * FROM thumb8")
    thumb9_comment_update = db.execute("SELECT * FROM thumb9")


    rows = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])
    session["user_username"] = rows[0]["username"]
    session["user_nickname"] = rows[0]["nickname"]
    rows = db.execute("SELECT * FROM all_comments_likes WHERE name = 'total'")
    comments_number = rows[0]["comments"]
    likes_number = rows[0]["likes"]
    rows = db.execute("SELECT * FROM all_comments_likes")


 # Update likes
    thumb1_like_update = db.execute("SELECT * FROM 'thumb1 likes' WHERE id = :id", id=session["user_id"])
    thumb2_like_update = db.execute("SELECT * FROM 'thumb2 likes' WHERE id = :id", id=session["user_id"])
    thumb3_like_update = db.execute("SELECT * FROM 'thumb3 likes' WHERE id = :id", id=session["user_id"])
    thumb4_like_update = db.execute("SELECT * FROM 'thumb4 likes' WHERE id = :id", id=session["user_id"])
    thumb5_like_update = db.execute("SELECT * FROM 'thumb5 likes' WHERE id = :id", id=session["user_id"])
    thumb6_like_update = db.execute("SELECT * FROM 'thumb6 likes' WHERE id = :id", id=session["user_id"])
    thumb7_like_update = db.execute("SELECT * FROM 'thumb7 likes' WHERE id = :id", id=session["user_id"])
    thumb8_like_update = db.execute("SELECT * FROM 'thumb8 likes' WHERE id = :id", id=session["user_id"])
    thumb9_like_update = db.execute("SELECT * FROM 'thumb9 likes' WHERE id = :id", id=session["user_id"])

    if request.method == "GET":
        return render_template("index.html", nickname=session["user_nickname"],
                                user_id=session["user_id"],
                                total_comments=comments_number, total_likes =likes_number,
                                comments_id=rows,
                                thumb1=thumb1_comment_update,thumb2=thumb2_comment_update,
                                thumb3=thumb3_comment_update,thumb4=thumb4_comment_update,
                                thumb5=thumb5_comment_update,thumb6=thumb6_comment_update,
                                thumb7=thumb7_comment_update,thumb8=thumb8_comment_update,
                                thumb9=thumb9_comment_update,
                                thumb1_liked=thumb1_like_update,thumb2_liked=thumb2_like_update,
                                thumb3_liked=thumb3_like_update,thumb4_liked=thumb4_like_update,
                                thumb5_liked=thumb5_like_update,thumb6_liked=thumb6_like_update,
                                thumb7_liked=thumb7_like_update,thumb8_liked=thumb8_like_update,
                                thumb9_liked=thumb9_like_update)

    if request.method == "POST":
        like = request.form.get("like")
        if like:
            likes =  request.form.get("id")
            id = " ".join((likes, "likes"))
            db.execute("INSERT INTO :id (id, nickname, likes) VALUES (:user_id, :user_nickname, :user_like)",
                    id=id, user_id=session["user_id"], user_nickname=session["user_nickname"], user_like=like)

            likes_number = likes_number + 1
            db.execute("UPDATE all_comments_likes SET likes = :number WHERE name = 'total'", number=likes_number)

            rows = db.execute("SELECT * FROM all_comments_likes WHERE name = :id", id=likes)
            likes_id = rows[0]["likes"] + 1

            db.execute("UPDATE all_comments_likes SET likes = :number WHERE name = :id", number=likes_id, id=likes)


        else:
            comment = request.form.get("comment")
            id = request.form.get("id")
            db.execute("INSERT INTO :id (id, nickname, comment) VALUES (:user_id, :user_nickname, :user_comment)",
                    id=id, user_id=session["user_id"], user_nickname=session["user_nickname"], user_comment=comment)

            comments_number = comments_number + 1
            db.execute("UPDATE all_comments_likes SET comments = :number WHERE name = 'total'", number=comments_number)

            rows = db.execute("SELECT * FROM all_comments_likes WHERE name = :id", id=id)
            comments_id = rows[0]["comments"] + 1

            db.execute("UPDATE all_comments_likes SET comments = :number WHERE name = :id", number=comments_id, id=id)

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
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

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

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        if len(rows) != 0 :
            return apology("this username is taken :(", 403)

        pas1 = request.form.get("password")
        pas2 = request.form.get("confirmPassword")
        if pas1 != pas2:
            pas1 = ""
            pas2 = ""
            return apology("passwords don't match", 403)

        pas1 = ""
        pas2 = ""


        nicknames = db.execute("SELECT * FROM users WHERE nickname = :nickname",
                      nickname=request.form.get("nickname"))

        if len(nicknames) != 0 :
            return apology("this nickname is taken :(", 403)

        db.execute("INSERT INTO users (username, nickname, hash) VALUES (:username, :nickname, :password)",
                    username=request.form.get("username"),
                    nickname=request.form.get("nickname"),
                    password=generate_password_hash(request.form.get("password")))


        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    if request.method == "GET":
        stage = 'get'
        return render_template("account.html", username=session["user_username"], stage=stage)

    new_nickname = request.form.get("nickname")
    rows = db.execute("SELECT * from users WHERE nickname = :nickname", nickname=new_nickname)
    if len(rows) != 0:
        stage = 'taken'
        return render_template("account.html", username=session["user_username"], stage=stage)


    # Updating nickname in users
    db.execute("UPDATE users SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])

    # Updating nickname in all the posts
    db.execute("UPDATE thumb1 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb2 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb3 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb4 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb5 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb6 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb7 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb8 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])
    db.execute("UPDATE thumb9 SET nickname = :nickname WHERE id = :id", nickname=new_nickname, id=session["user_id"])

    stage = 'success'

    return render_template("account.html", stage=stage)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
