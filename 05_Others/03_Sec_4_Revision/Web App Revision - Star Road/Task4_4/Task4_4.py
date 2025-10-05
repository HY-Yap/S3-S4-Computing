from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['name']
        query = '''
        SELECT Relic.Name, Position, RelicSet.Name, SetEffect, Relic.Stats FROM Relic
        INNER JOIN RelicSet
        ON Relic.SetID = RelicSet.ID
        INNER JOIN Equipment
        ON Equipment.RelicID = Relic.ID
        INNER JOIN Character
        ON Equipment.CharacterID = Character.id
        WHERE Character.name = ?
        '''
        conn = sqlite3.connect('star_road.db')
        cursor = conn.execute(query, (name,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('result.html', name=name, data=data)

if __name__ == '__main__':
    app.run(debug=True)
