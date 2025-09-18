from flask import Flask, render_template, request
import os
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


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form/', methods=["GET", "POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        # based on class_, tabulate data from the database
        # subj count for fav_subj
        class_name = request.form.get('class_')

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        # method 1 - using GROUP BY and COUNT
        # query = """
        # SELECT Fav_Subj, COUNT(*) as count
        # FROM Survey
        # WHERE Class = ?
        # GROUP BY Fav_Subj
        # ORDER BY count DESC
        # """

        # cursor.execute(query, (class_name,))
        # data = cursor.fetchall()

        # conn.close()

        # method 2 - Query all data and process in Python
        query = "SELECT Fav_Subj FROM Survey WHERE Class = ?"
        cursor.execute(query, (class_name,))
        data = cursor.fetchall()
        conn.close()
        # Count occurrences of each favorite subject
        subject_count = {}
        for row in data:
            subject = row[0]
            if subject in subject_count:
                subject_count[subject] += 1
            else:
                subject_count[subject] = 1
        # Convert to list of tuples for rendering
        result = []
        for subj in subject_count:
            result.append((subj, subject_count[subj]))

        # Sort the result by count in descending order
        result.sort(key=lambda x: x[1], reverse=True)

        # Render the results in a new template
        return render_template(
            "result.html",
            class_=class_name,
            data=result
        )


@app.route('/store/', methods=["GET", "POST"])
def store():
    if request.method == "GET":
        return render_template("store.html", stores=STORES)
    else:
        store_name = request.form.get('store')

        # method 1 - Query all studnts in one query
        # conn = sqlite3.connect(db_file)
        # query = """
        # SELECT Class, Name
        # FROM Survey
        # WHERE Fav_Store = ?
        # """

        # cursor = conn.execute(query, (store_name,))
        # data = cursor.fetchall()
        # cursor.close()
        # conn.close()

        # # randomly select 2 student representatives
        # sec3_students = []
        # sec4_students = []

        # for student in data:
        #     if student[0] in SEC3_CLASSES:
        #         sec3_students.append(student)
        #     elif student[0] in SEC4_CLASSES:
        #         sec4_students.append(student)

        # method 2 - Query each level separately
        conn = sqlite3.connect(db_file)
        query = """
        SELECT Name, Class
        FROM Survey
        WHERE Fav_Store = ?
        AND Class IN (?, ?, ?)
        """

        # Method 3 - Like keyword with flexible search
        # '3A%' means all strings starting with 3A
        query = """
        SELECT Name, Class
        FROM Survey
        WHERE Fav_Store = ?
        AND Class Like '3A%'
        """

        cursor = conn.execute(query, (store_name, *SEC3_CLASSES))
        sec3_students = cursor.fetchall()
        cursor = conn.execute(query, (store_name, *SEC4_CLASSES))
        sec4_students = cursor.fetchall()
        cursor.close()
        conn.close()

        # randomly select 2 student representatives
        sec3_rep = random.choice(sec3_students)
        sec4_rep = random.choice(sec4_students)

        return render_template(
            "student.html",
            store=store_name,
            sec3_rep=sec3_rep,
            sec4_rep=sec4_rep
        )


if __name__ == '__main__':
    app.run(debug=True)
