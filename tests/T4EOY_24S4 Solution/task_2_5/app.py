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

        # level_class_count = len(result["Sec 1"])
        # print(result)
        return render_template(
            "result.html",
            team_name=team_name,
            data=data
        )


@app.route("/rank/")
def rank():
    query = """
    SELECT Teams.Name, Teams.School,
    SUM(Kills) AS TotalKills,
    SUM(Deaths) AS TotalDeaths,
    SUM(Assists) AS TotalAssists
    FROM GameStats
    INNER JOIN Players
    ON GameStats.PlayerID = Players.PlayerID
    INNER JOIN TeamRosters
    ON Players.PlayerID = TeamRosters.PlayerID
    INNER JOIN Teams
    ON Teams.TeamID = TeamRosters.TeamID
    GROUP BY Teams.Name
    ORDER BY TotalKills DESC
    """

    conn = sqlite3.connect("esports.db")
    cursor = conn.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # process kda
    for i in range(len(data)):
        row = data[i]
        k, d, a = row[2], row[3], row[4]
        kda = round((k + a) / d, 1)
        data[i] = tuple(row) + (kda,)
        # print(data[i])

    return render_template(
        "ranking.html",
        data=data
    )


@app.route("/school/<team_name>/")
def school(team_name):
    query = """
    SELECT Players.Nickname, Players.Role,
    SUM(GameStats.Kills) AS TotalKills,
    SUM(GameStats.Deaths) AS TotalDeaths,
    SUM(GameStats.Assists) AS TotalAssists
    FROM GameStats
    INNER JOIN Players
    ON GameStats.PlayerID = Players.PlayerID
    INNER JOIN TeamRosters
    ON Players.PlayerID = TeamRosters.PlayerID
    INNER JOIN Teams
    ON Teams.TeamID = TeamRosters.TeamID
	WHERE Teams.Name = ?
    GROUP BY Players.Nickname
    ORDER BY TotalKills DESC
    """

    conn = sqlite3.connect("esports.db")
    cursor = conn.execute(query, (team_name,))
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    # process kda
    for i in range(len(data)):
        row = data[i]
        k, d, a = row[2], row[3], row[4]
        kda = round((k + a) / d, 1)
        data[i] = tuple(row) + (kda,)
        # print(data[i])

    return render_template(
        "school.html",
        team_name=team_name,
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)
