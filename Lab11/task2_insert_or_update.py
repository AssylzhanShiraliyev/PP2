import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Assylzhan2007"
)
cursor = connection.cursor()

name = input("Enter user name: ")
phone = input("Enter phone number: ")

cursor.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
connection.commit()

print("User added or updated.")

cursor.close()
connection.close()
