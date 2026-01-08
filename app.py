from flask import Flask, render_template, request, redirect, url_for, session
from database import create_tables
import models
import pickle
from auth import auth

app = Flask(__name__)
app.secret_key = "secret"
app.register_blueprint(auth)

create_tables()
model = pickle.load(open("model.pkl","rb"))

def login_required():
    return "user" in session

@app.route("/")
def index():
    if "user" not in session:
        return redirect("/login")

    students = models.get_all_students()
    total, departments, final_year = models.get_stats()

    return render_template(
        "index.html",
        students=students,
        total=total,
        departments=departments,
        final_year=final_year
    )


@app.route("/search")
def search():
    q = request.args.get("q")
    students = models.search_students(q)
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        models.add_student(
            request.form["name"],
            request.form["roll"],
            request.form["dept"],
            request.form["year"]
        )
        return redirect("/")
    return render_template("add_student.html")

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        models.update_student(
            id,
            request.form["name"],
            request.form["roll"],
            request.form["dept"],
            request.form["year"]
        )
        return redirect("/")
    return render_template("edit_student.html", student=models.get_student(id))

@app.route("/delete/<int:id>")
def delete(id):
    models.delete_student(id)
    return redirect("/")

@app.route("/predict", methods=["GET","POST"])
def predict():
    result = None
    if request.method == "POST":
        marks = int(request.form["marks"])
        result = "PASS" if model.predict([[marks]])[0] else "FAIL"
    return render_template("predict.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
