from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/student/")
def student():
    return render_template("student.html")

@app.route("/teacher/")
def teacher():
    return render_template("teacher.html")

@app.route("/display/<role>/")
def display(role):
    if role == "student":
        return f"URL for student is: {url_for(role)}"

if __name__ == "__main__":
    app.run(debug=True)
