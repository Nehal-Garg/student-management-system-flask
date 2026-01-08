from flask import Blueprint, render_template, request, redirect, session
import hashlib, sqlite3

auth = Blueprint("auth", __name__)

def get_db():
    return sqlite3.connect("students.db")

@auth.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = hashlib.sha256(request.form["password"].encode()).hexdigest()

        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (u, p)
        ).fetchone()

        if user:
            session["user"] = u
            return redirect("/")
        return "Invalid credentials"

    return render_template("login.html")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect("/login")
