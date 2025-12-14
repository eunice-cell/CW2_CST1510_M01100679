# loading the dataset table

import sqlite3
databaseLoc = "../database/intelligence_platform.db"


def load_datasets():
    print("Loading datasets")


conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

cursor.execute("DELETE FROM datasets")

with open('../database/datasets_metadata.csv', 'r') as datas:
    i = 0
    for line in datas.readlines():
        if i == 0:
            i += 1
            continue
        line = line.strip()
        vals = line.split(',')
        cursor.execute("""INSERT OR IGNORE INTO datasets(
                 name ,rows ,columns, uploaded_by ,date )
            values(?,?,?,?,?)""", (vals[1], vals[2], vals[3], vals[4], vals[5]))

conn.commit()
conn.close()


# loading incidents table
def load_incidents():
    print("Loading cyber incidents...")


conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('../database/cyber_incidents.csv', 'r') as cyber:
    i = 0
    for line in cyber.readlines():
        if i == 0:
            i += 1
            continue
        line = line.strip()
        vals = line.split(',')
        cursor.execute("""INSERT INTO cyber_incidents(
                 i_date,i_type,status,description,reported_by)
            values(?,?,?,?,?)""", (vals[1], vals[2], vals[3], vals[4], vals[5]))
conn.commit()
conn.close()


# load tickets table
def load_tickets():
    print("Loading IT tickets...")


conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

with open('../database/it_tickets.csv', 'r') as cyber:
    i = 0
    for line in cyber.readlines():
        if i == 0:
            i += 1
            continue
        line = line.strip()
        vals = line.split(',')
        cursor.execute("""INSERT INTO tickets(
             priority, description, status, created_at, created_date)
            values(?,?,?,?,?)""", (vals[1], vals[2], vals[3], vals[4], vals[5]))
conn.commit()
conn.close()


# users table
def load_users():
    print("Loading users...")


conn = sqlite3.connect(databaseLoc)
cursor = conn.cursor()

cursor.execute("DELETE FROM users")

with open('../database/users.txt', 'r') as user:
    i = 0
    for line in user.readlines():
        line = line.strip()
        vals = line.split(',')
        cursor.execute(
            """INSERT OR IGNORE INTO users(
        username ,password_hash ,role ) values(?,?,?)""", (vals[0], vals[1], 'user'))

conn.commit()
conn.close()
# this means that if we run in main.py it will not appear only when u run this page
#which is good cause we don't want this to interfere with our OOP
if __name__ == "__main__":
    load_users()
    load_datasets()
    load_incidents()
    load_tickets()
    print("All data imported successfully!")
