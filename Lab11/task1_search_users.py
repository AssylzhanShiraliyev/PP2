import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Assylzhan2007"
)
cursor = connection.cursor()

pattern = input("Enter pattern to search (name or phone): ")

cursor.execute("SELECT * FROM search_users(%s);", (pattern,))
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
