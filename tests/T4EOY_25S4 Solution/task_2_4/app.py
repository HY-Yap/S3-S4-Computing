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
        team_name = request.form["team_name"]
        query = """
        SELECT GameID, Teams.Name, Players.Name,
        Nickname, Kills, Deaths, Assists
        FROM GameStats
        INNER JOIN Players
        ON GameStats.PlayerID = Players.PlayerID
        INNER JOIN TeamRosters
        ON Players.PlayerID = TeamRosters.PlayerID
        INNER JOIN Teams
        ON Teams.TeamID = TeamRosters.TeamID
        WHERE Teams.Name = ?
        ORDER BY GameID
        """

        conn = sqlite3.connect("esports.db")
        cursor = conn.execute(query, (team_name,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        return render_template(
            "result.html",
            team_name=team_name,
            data=data
        )


if __name__ == "__main__":
    app.run(debug=True)
