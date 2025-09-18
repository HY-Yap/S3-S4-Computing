from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search/', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        cid = request.form['cid']
        # print(cid)
        conn = sqlite3.connect('insurance.db')
        query = """
        SELECT * FROM PolicyRecord
        WHERE CustomerID = ?
        """
        cursor = conn.execute(query, (cid,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('results.html', cid=cid, data=data)

@app.route('/policy/<pid>/')
def policy(pid):
    conn = sqlite3.connect('insurance.db')
    query = """
    SELECT * FROM Policy
    WHERE PolicyID = ?
    """
    cursor = conn.execute(query, (pid,))
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('policy.html', pid=pid, data=data)

@app.route('/team/', methods=['GET','POST'])
def team():
    if request.method == 'GET':
        return render_template('team.html')
    else:
        tid = request.form['tid']
        conn = sqlite3.connect('insurance.db')
        query = """
        SELECT AgentID, Name, BaseSalary FROM Agent
        WHERE TeamNo = ?
        """
        cursor = conn.execute(query, (tid,))
        agents = cursor.fetchall()
        cursor.close()
        conn.close()

        for agent in agents:
            aid, name, base_salary = agent
            conn = sqlite3.connect('insurance.db')
            query = """
            
            """
            cursor = conn.execute(query, (aid, name, base_salary))
            data = cursor.fetchone()
            cursor.close()
            conn.close()
        return render_template('earnings.html', tid=tid, data=data)

if __name__ == '__main__':
    app.run(debug=True)
