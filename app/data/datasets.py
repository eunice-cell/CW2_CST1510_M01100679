import sqlite3
databaseLoc= '../../DATA/intelligence_platform.db'
conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('../../DATA/datasets_metadata.csv', 'r') as datas:
       i = 0
       for line in datas.readlines():
           if i == 0:
               i += 1
               continue
           line = line.strip()
           vals = line.split(',')
           cursor.execute("""INSERT INTO datasets(
                 name ,rows ,columns, uploaded_by ,date )
            values(?,?,?,?,?)""",(vals[1],vals[2], vals[3], vals[4], vals[5]))
conn.commit()
