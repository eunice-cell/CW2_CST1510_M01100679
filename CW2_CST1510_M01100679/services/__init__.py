from services.database_manager import DatabaseManager

db_path = "C:/Users/HP/PycharmProjects/CW2_CST1510_M01100679/database/intelligence_platform.db"
db = DatabaseManager(db_path)
db.connect()
cursor = db.execute_query("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)
db.close()
