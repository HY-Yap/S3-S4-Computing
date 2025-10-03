from flask import Flask, request, render_template
import sqlite3
import random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "GET":
        conn = sqlite3.connect("hotel_booking.db")
        query = """
        SELECT * FROM RoomType
        """
        cursor = conn.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template(
            "form.html",
            data=data
        )
    else:
        # read the submitted data
        room_type_id = request.form["room_type_id"]
        cust_id = request.form["cust_id"]
        start_date = request.form["start_date"]
        no_of_days = request.form["no_of_days"]
        # print(room_type_id, cust_id, start_date, no_of_days)
        # remove "-" in date
        start_date = start_date.replace("-", "")

        # check db, find rooms based on room_type_id
        conn = sqlite3.connect("hotel_booking.db")
        query = """
        SELECT RoomID FROM Room
        WHERE RoomTypeID = ?
        """
        cursor = conn.execute(query, (room_type_id,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        # print(data)

        # randomly allocate 1 room
        room_id = random.choice(data)[0]
        # print(room_id)

        # create the booking record
        conn = sqlite3.connect("hotel_booking.db")
        query = """
        INSERT INTO BookingRecord
        (RoomID, CustomerID, StartDate, NoOfDays)
        VALUES
        (?,?,?,?)
        """
        conn.execute(
            query,
            (room_id, cust_id, start_date, no_of_days))
        conn.commit()
        conn.close()

        # render confirmation
        return render_template(
            "confirm.html",
            conf_tpl=(room_id, cust_id, start_date, no_of_days)
        )


if __name__ == "__main__":
    app.run(debug=True)
