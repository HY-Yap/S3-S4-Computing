from flask import Flask, render_template, request
import sqlite3
import csv

# Task 1.1

db_file = 'property.db'

query1 = """
CREATE TABLE IF NOT EXISTS "User" (
	"UserID"	TEXT NOT NULL,
	"Name"	TEXT NOT NULL,
	"Contact"	INTEGER NOT NULL,
	"Email"	TEXT NOT NULL,
	PRIMARY KEY("UserID")
);
"""

query2 = """
CREATE TABLE IF NOT EXISTS "Property" (
	"PropertyID"	TEXT NOT NULL,
	"Address"	TEXT NOT NULL,
	"Postal"	INTEGER NOT NULL,
	"TotalArea"	INTEGER NOT NULL,
	"NoOfBedroom"	INTEGER NOT NULL,
	"NoOfToilet"	INTEGER NOT NULL,
	"AskingPrice"	REAL NOT NULL,
	"Status"	TEXT NOT NULL DEFAULT 'FALSE' CHECK("Status" IN ('TRUE', 'FALSE')),
	PRIMARY KEY("PropertyID")
);
"""

query3 = """
CREATE TABLE IF NOT EXISTS "Record" (
	"RecordID"	INTEGER NOT NULL,
	"SellerID"	TEXT NOT NULL,
	"PropertyID"	TEXT NOT NULL,
	"DateListed"	TEXT NOT NULL,
	"BuyerID"	TEXT,
	"SoldPrice"	REAL,
	"SoldDate"	TEXT,
	PRIMARY KEY("RecordID" AUTOINCREMENT)
);
"""

queries = [query1, query2, query3]

def create_db():
    conn = sqlite3.connect(db_file)
    for query in queries:
        conn.execute(query)
    conn.commit()
    conn.close()

# --------------------------------------------------#
# * RUN TASK 1.1
# create_db()
# --------------------------------------------------#

# Task 1.2

files = {
    'Property': 'properties.csv',
    'Record': 'records.csv',
    'User': 'users.csv'
}

def import_data(files):
    for table in files:
        with open(f'data_files/{files[table]}', 'r') as f:
            csv_reader = csv.reader(f, delimiter=';')
            header = next(csv_reader)
            fields = ','.join(header)
            for row in csv_reader:
                conn = sqlite3.connect(db_file)
                ph = ','.join(['?' for _ in row])
                query = f"""
                INSERT INTO {table}
                ({fields})
                VALUES
                ({ph})
                """
                try:
                    print(query)
                    print(tuple(row))
                    conn.execute(query, tuple(row))
                    print('added')
                except:
                    continue
                conn.commit()
                conn.close()


# --------------------------------------------------#
# * RUN TASK 1.2
# import_data(files=files)
# --------------------------------------------------#

# Task 1.3

query = """
SELECT RecordID, Record.PropertyID, Address, TotalArea, NoOfBedroom, NoOfToilet, AskingPrice FROM Record
INNER JOIN Property
ON Record.PropertyID = Property.PropertyID
INNER JOIN User
ON Record.BuyerID = User.UserID
WHERE Property.Status = 'TRUE' AND Property.NoOfBedroom = 3 AND Property.NoOfToilet = 3
ORDER BY Property.AskingPrice DESC
"""

def task1_3():
    conn = sqlite3.connect(db_file)
    cursor = conn.execute(query)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in data:
        print(row)

# --------------------------------------------------#
# * RUN TASK 1.3
# task1_3()
# --------------------------------------------------#

# Task 1.4

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        recordID = request.form['recordID']
        buyerID = request.form['buyerID']
        soldPrice = request.form['soldPrice']
        soldDate = request.form['soldDate']
        tup1 = (buyerID, soldPrice, soldDate, recordID)
        tup2 = (recordID, buyerID, soldPrice, soldDate)

        # update Record
        update_record = """
        UPDATE Record
        SET BuyerID = ?, SoldPrice = ?, SoldDate = ?
        WHERE RecordID = ?
        """
        conn = sqlite3.connect(db_file)
        conn.execute(update_record, tup1)
        conn.commit()
        conn.close()

        # retrieve PropertyID
        retrieve_pid = """
        SELECT PropertyID FROM Record
        WHERE RecordID = ?
        """
        conn = sqlite3.connect(db_file)
        cursor = conn.execute(retrieve_pid, (recordID,))
        pid = cursor.fetchone()
        cursor.close()
        conn.close()

        print(pid)

        # update Property
        update_property = """
        UPDATE Property
        SET Status = 'TRUE'
        WHERE PropertyID = ?
        """
        conn = sqlite3.connect(db_file)
        conn.execute(update_property, pid)
        conn.commit()
        conn.close()

        # display data
        retrieve_data = """
        SELECT User.UserID, User.Name, User.Contact, User.Email, Property.PropertyID, Property.Address, Property.Postal, Property.TotalArea, Property.NoOfBedroom, Property.NoOfToilet, Property.AskingPrice, Property.Status FROM User
        INNER JOIN Record
        ON User.UserID = Record.BuyerID
        INNER JOIN Property
        ON Record.PropertyID = Property.PropertyID
        WHERE Record.RecordID = ? AND Record.BuyerID = ? AND Record.SoldPrice = ? AND Record.SoldDate = ?
        """
        conn = sqlite3.connect(db_file)
        cursor = conn.execute(retrieve_data, tup2)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return render_template('result.html', data=data, soldPrice=soldPrice, soldDate=soldDate, recordID=recordID)

# --------------------------------------------------#
# * RUN TASK 1.4
if __name__ == "__main__":
    app.run(debug=True)
# --------------------------------------------------#
