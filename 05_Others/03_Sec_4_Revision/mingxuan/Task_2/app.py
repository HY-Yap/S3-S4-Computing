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
        title = request.form['title']
        # print(f'title: {title}')
        conn = sqlite3.connect('readtrack.db')
        query = """
        SELECT Member.Class, COUNT(Member.IndexNo) FROM Member
        INNER JOIN ReadingLog
        ON Member.MemberID = ReadingLog.MemberID
        INNER JOIN Book
        ON ReadingLog.BookID = Book.BookID
        WHERE Book.Title = ?
        GROUP BY Member.Class
        """
        cursor = conn.execute(query, (title,))
        data = cursor.fetchall()
        total = 0
        for row in data:
            total += row[1]
        cursor.close()
        conn.close()
        return render_template('result.html', title=title, data=data, total=total)

if __name__ == '__main__':
    app.run(debug=True)
