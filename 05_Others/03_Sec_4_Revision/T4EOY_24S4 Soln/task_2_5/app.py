import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    elif request.method == "POST":
        cname = request.form["name"]
        query = """
        SELECT Class, Count(Class) AS ClassCount
        FROM Vote
        INNER JOIN Candidate
        ON Vote.CandidateNo = Candidate.CandidateNo
        INNER JOIN Student
        ON Vote.MatricNo = Student.MatricNo
        WHERE Candidate.Name = ?
        GROUP BY Class
        ORDER BY Class ASC, IndexNo ASC
        """

        conn = sqlite3.connect("voting_mgm.db")
        cursor = conn.execute(query, (cname,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        # level_class_count = len(result["Sec 1"])
        # print(result)
        return render_template(
            "result.html",
            cname=cname,
            data=data
        )


if __name__ == "__main__":
    app.run(debug=True)
