import sqlite3
databaseLoc='../../DATA/intelligence_platform.db'
conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('../../DATA/users.txt', 'r') as user:
       i = 0
       for line in user.readlines():

           line = line.strip()
           vals = line.split(',')
           cursor.execute(
               """INSERT INTO users(
           username ,password_hash ,role ) values(?,?,?)""",(vals[0], vals[1],'user'))

conn.commit()