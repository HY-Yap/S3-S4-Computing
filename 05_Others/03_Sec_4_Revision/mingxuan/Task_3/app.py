from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        cclass = request.form['class']
        gender = request.form['gender']
        conn = sqlite3.connect('readtrack.db')
        query = """
        SELECT Member.MemberID, Member.IndexNo, GROUP_CONCAT(Book.Genre) FROM Member
        INNER JOIN ReadingLog
        ON Member.MemberID = ReadingLog.MemberID
        INNER JOIN Book
        ON Book.BookID = ReadingLog.BookID
        WHERE Member.Class = ? AND Member.Gender = ?
        GROUP BY IndexNo
        """
        cursor = conn.execute(query, (cclass, gender))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('result.html', data=data)

@app.route('/info/<mid>')
def info(mid):
    return render_template('info.html', mid=mid)

if __name__ == '__main__':
    app.run(debug=True)
