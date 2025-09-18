import os
from flask import Flask, render_template, request
import sqlite3
import random


# Hint1: please use db_file instead of typing the file name
# this will help you to avoid potential errors
curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, 'survey.db')


# Hint2: You may use the following variables for your convenience
STORES = [
    'Jap Food', 'Mixed Vege', 'Western Delight',
    'Chicken Rice', 'K Food', 'Local Delight',
    'Drink Store'
]

SEC3_CLASSES = ('3A1', '3A2', '3A3')
SEC4_CLASSES = ('4A1', '4A2', '4A3')

# Your code here
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        cls = request.form['cls']
        conn = sqlite3.connect(db_file)
        query = """
        SELECT Fav_Subj, COUNT(Fav_Subj) AS Count FROM Survey
        WHERE Class = ?
        GROUP BY Fav_Subj
        ORDER BY Count DESC
        """
        cursor = conn.execute(query, (cls,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('results.html', cls=cls, data=data)

@app.route('/store/', methods=['GET', 'POST'])
def store():
    if request.method == 'GET':
        return render_template('store.html')
    else:
        store = request.form['store']
        conn = sqlite3.connect(db_file)
        query = """
        SELECT Name FROM Survey
        WHERE Fav_Store = ? AND Class = ?
        """

        reps = []

        students = []
        for cls in SEC3_CLASSES:
            cursor = conn.execute(query, (store, cls))
            data = cursor.fetchall()
            for row in data:
                students.append(row[0])
            cursor.close()
            conn.close()
        reps.append(random.random(students))

        students = []
        for cls in SEC4_CLASSES:
            cursor = conn.execute(query, (store, cls))
            data = cursor.fetchall()
            for row in data:
                students.append(row[0])
            cursor.close()
            conn.close()
        reps.append(random.random(students))

        return reps

if __name__ == '__main__':
    app.run(debug=True)
