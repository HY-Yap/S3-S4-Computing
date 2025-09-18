import sqlite3
import os
from flask import Flask, render_template, request

# get abs path to curr folder
curr_dir = os.path.dirname(os.path.abspath(__file__))
# get abs path to db
db_file = os.path.join(curr_dir, "insurance.db")


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        # render form
        return render_template("form.html")
    else:
        # receive form submission
        # 1. get the form submission value
        cust_id = request.form["cust_id"]

        # 2. query db
        conn = sqlite3.connect(db_file)
        query = """
        SELECT * FROM PolicyRecord
        WHERE CustomerID = ?
        """
        cursor = conn.execute(query, (cust_id,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()

        # 3. render to result
        return render_template(
            "result.html",
            cust_id=cust_id,
            data=data
        )


@app.route("/policy/<policy_id>/")
def policy(policy_id):
    # query db, get info on this policy
    conn = sqlite3.connect(db_file)
    query = """
    SELECT * FROM Policy
    WHERE PolicyID = ?
    """
    cursor = conn.execute(query, (policy_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    # render to html
    return render_template(
        "policy.html",
        row=row
    )


@app.route("/team/", methods=["GET", "POST"])
def team():
    if request.method == "GET":
        return render_template("team.html")
    else:
        # 1. query using team_no
        team_no = request.form["team_no"]
        # get AgentID, Name, BaseSalary
        conn = sqlite3.connect(db_file)
        query = """
        SELECT AgentID, Name, BaseSalary
        FROM Agent
        WHERE TeamNo = ?
        """
        cursor = conn.execute(query, (team_no,))
        agents = cursor.fetchall()
        cursor.close()
        conn.close()

        # 2. for each agent
        # for each month
        # calculate the earning = base + commission
        months = ["20200101", "20200201", "20200301", "20200401"]
        result = []
        for agent in agents:
            agent_id, name, base = agent

            row = [name]
            for i in range(3):
                month_start = months[i]
                month_end = months[i+1]
                conn = sqlite3.connect(db_file)
                query = """
                SELECT SUM(ProtectedSum*CommissionRate)
                FROM Policy
                INNER JOIN PolicyRecord
                ON Policy.PolicyID = PolicyRecord.PolicyID
                WHERE AgentID = ?
                AND StartDate >= ?
                AND StartDate < ?
                GROUP BY AgentID
                """
                cursor = conn.execute(
                    query,
                    (agent_id, month_start, month_end)
                )
                commission = cursor.fetchone()
                # print(commission)
                if commission is None:
                    commission = 0
                else:
                    commission = commission[0]
                cursor.close()
                conn.close()
                earning = base + commission
                row.append(earning)
            result.append(row)

        # print(result)

        # 3. render
        return render_template(
            "earning.html",
            team_no=team_no,
            result=result
        )


if __name__ == "__main__":
    app.run(debug=True)
