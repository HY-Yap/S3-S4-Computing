import sqlite3
import csv

files = {
    'Character': 'characters.csv', 
    'RelicSet': 'relic_sets.csv',
    'Relic': 'relics.csv',
    'Equipment': 'equipments.csv'
}

for file in files:
    with open(f'data_files/{files[file]}', 'r') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)
        ph = ','.join('?' for _ in header)
        # print(file)
        # print(header)
        # print(ph)
        query = f'''
        INSERT INTO {file}
        ({','.join(_ for _ in header)})
        VALUES
        ({ph})
        '''
        # print(query)
        conn = sqlite3.connect('star_road.db')
        for row in csv_reader:
            conn.execute(query, tuple(row))
        conn.commit()
        conn.close()
