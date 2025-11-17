import sqlite3
databaseLoc='../../DATA/intelligence_platform.db'
conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('../../DATA/it_tickets.csv', 'r') as cyber:
       i = 0
       for line in cyber.readlines():
           if i == 0:
               i += 1
               continue
           line = line.strip()
           vals = line.split(',')
           cursor.execute( """INSERT INTO tickets(
             priority, description, status, created_at, created_date)
            values(?,?,?,?,?)""",(vals[1], vals[2], vals[3], vals[4], vals[5]))
conn.commit()
