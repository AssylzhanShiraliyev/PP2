import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Assylzhan2007"
)
cursor = connection.cursor()

count = int(input("How many users do you want to insert? "))
users = []

for _ in range(count):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    users.append([name, phone])

cursor.execute("CALL insert_many_users(%s);", (users,))
connection.commit()

print("Users inserted (invalid phones ignored inside procedure).")

cursor.close()
connection.close()
