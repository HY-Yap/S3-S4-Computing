# * update this from ggl classroom

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def get_db():
    db = sqlite3.connect("message.db")
    print("DB opened successfully.")
    return db


def create_db():
    db = get_db()
    query = """
    CREATE Table IF NOT EXISTS posting (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    message TEXT
    )
    """
    db.execute(query)
    db.commit()
    db.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        # loading the form page
        return render_template("form.html")
    else:
        # POST request form submission
        # print(request.form)
        username = request.form["username"]
        email = request.form["email"]
        message = request.form["message"]

        db = get_db()
        query = """
        INSERT INTO posting
        (username, email, message)
        VALUES
        (?, ?, ?)
        """
        db.execute(
            query,
            (username, email, message)
        )
        db.commit()
        db.close()

        return redirect(url_for("success"))


@app.route("/update/<int:rid>/", methods=["GET", "POST"])
def update(rid):
    if request.method == "GET":
        # GET method: display the update sheet
        # 1. read current row based on rid from db
        db = get_db()
        query = "SELECT * FROM posting WHERE id = ?"
        cursor = db.execute(query, (rid,))
        row = cursor.fetchone()
        # row = cursor.fetchall()[0]
        cursor.close()
        db.close()
        # 2. render update html
        return render_template(
            "update.html",
            row=row
        )
    else:
        # POST method: receive the values, and update db
        # 1. retrieve from request.form
        message = request.form["message"]

        # 2. update db
        db = get_db()
        query = """
        UPDATE posting
        SET message = ?
        WHERE id = ?
        """
        db.execute(query, (message, rid))
        db.commit()
        db.close()

        # 3. redirect back to message board
        return redirect(url_for("success"))


@app.route("/delete/<int:rid>/", methods=["GET", "POST"])
def delete(rid):
    if request.method == "GET":
        # GET method: display the delete sheet
        # 1. read current row based on rid from db
        db = get_db()
        query = "SELECT * FROM posting WHERE id = ?"
        cursor = db.execute(query, (rid,))
        row = cursor.fetchone()
        # row = cursor.fetchall()[0]
        cursor.close()
        db.close()
        # 2. render delete html
        return render_template(
            "delete.html",
            row=row
        )
    else:
        # POST method: receive the values, and delete db
        # 1. retrieve from request.form

        # 2. delete db
        db = get_db()
        query = """
        DELETE FROM posting
        WHERE id = ?
        """
        db.execute(query, (rid,))
        db.commit()
        db.close()

        # 3. redirect back to message board
        return redirect(url_for("success"))


@app.route("/success/")
def success():
    # read the db
    db = get_db()
    query = "SELECT * FROM posting"
    cursor = db.execute(query)
    data = cursor.fetchall()
    cursor.close()
    db.close()

    # pass data to render success page
    return render_template(
        "success.html",
        data=data
    )


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
