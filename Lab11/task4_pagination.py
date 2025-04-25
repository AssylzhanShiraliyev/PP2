import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Assylzhan2007"
)
cursor = connection.cursor()

limit = int(input("Enter limit (number of users to show): "))
offset = int(input("Enter offset (starting position): "))

cursor.execute("SELECT * FROM get_users(%s, %s);", (limit, offset))
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()
