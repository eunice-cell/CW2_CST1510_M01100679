import sqlite3
import csv
databaseLoc='../../DATA/intelligence_platform.db'
conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('../../DATA/cyber_incidents.csv', 'r') as cyber:
       i = 0
       for line in cyber.readlines():
           if i == 0:
               i += 1
               continue
           line = line.strip()
           vals = line.split(',')
           cursor.execute("""INSERT INTO cyber_incidents(
                 i_date,i_type,status,description,reported_by)
            values(?,?,?,?,?)""",( vals[1], vals[2], vals[3], vals[4], vals[5]))
conn.commit()
