import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="phonebook_db",
    user="postgres",
    password="Assylzhan2007"
)
cursor = connection.cursor()

identifier = input("Enter user name or phone to delete: ")

cursor.execute("CALL delete_user(%s);", (identifier,))
connection.commit()

print("User deleted if existed.")

cursor.close()
connection.close()
