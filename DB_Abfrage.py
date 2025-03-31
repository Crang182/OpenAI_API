import sqlite3

conn = sqlite3.connect("token_usage.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM token_usage WHERE model = 'gpt-4o'")
rows = cursor.fetchall()

for row in rows:
    print(row)


conn.close()