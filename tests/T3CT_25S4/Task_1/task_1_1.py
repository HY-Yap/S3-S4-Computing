import os
import sqlite3
import csv

# Hint1: please use db_file instead of typing the file name
# this will help you to avoid potential errors
curr_dir = os.path.dirname(os.path.abspath(__file__))
db_file = os.path.join(curr_dir, 'survey.db')

# Hint2: You may use the data_files list to retrieve
# the path to all files in the `data_files` folder
classes = ["3A1", "3A2", "3A3", "4A1", "4A2", "4A3"]
data_files = []
for cls in classes:
    path = os.path.join(
        curr_dir, 'data_files', f'class_{cls}.csv')
    data_files.append(path)


def create_table():
    """Create the Survey table in the SQLite database"""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Survey (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT NOT NULL,
            Class TEXT NOT NULL,
            Fav_Subj TEXT NOT NULL,
            Fav_Store TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("Survey table created successfully!")


def load_data():
    # Your code here:
    for cls in data_files:
        with open(cls, 'r') as f:
            # print(f'opened {cls}')
            csv_reader = csv.reader(f)
            header = next(csv_reader)
            data = []
            for row in csv_reader:
                data.append(row)
            fields = ','.join(header)
            # print(fields)
            for row in data:
                ph = ','.join(['?' for _ in row])
                conn = sqlite3.connect(db_file)
                query = f"""
                INSERT INTO Survey
                ({fields})
                VALUES
                ({ph})
                """              
                # print(query)
                conn.execute(query, tuple(row))
                conn.commit()
                conn.close()


if __name__ == '__main__':
    # Hint3: if your db is locked, delete it
    # rerun the following code to reset the database
    # create_table()

    load_data()
