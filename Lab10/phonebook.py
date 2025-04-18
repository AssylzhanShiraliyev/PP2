import csv
from database import connect_to_db, create_phonebook_table

class PhoneBook:
    def __init__(self):
        """Initialize phonebook with database connection"""
        self.conn = connect_to_db("phonebook")
        if self.conn:
            self.cur = self.conn.cursor()
            create_phonebook_table(self.conn)
    
    def insert_from_csv(self, filename):
        """Insert contacts from CSV file"""
        try:
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Skip header
                for row in reader:
                    self.cur.execute(
                        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                        (row[0], row[1], row[2])
                    )
            self.conn.commit()
            print(f"Successfully imported data from {filename}")
        except Exception as e:
            self.conn.rollback()
            print(f"CSV import error: {e}")

    def insert_from_console(self):
        """Add contact via user input"""
        print("\nEnter contact details:")
        first_name = input("First name: ").strip()
        last_name = input("Last name (optional): ").strip()
        phone = input("Phone number: ").strip()
        
        try:
            self.cur.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (first_name, last_name, phone)
            )
            self.conn.commit()
            print("Contact added successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Error adding contact: {e}")

    def update_contact(self):
        """Update existing contact's information"""
        phone = input("\nEnter phone number to update: ").strip()
        
        self.cur.execute("SELECT id FROM phonebook WHERE phone = %s", (phone,))
        if not self.cur.fetchone():
            print("Contact not found")
            return
        
        print("Select field to update:")
        print("1. First name")
        print("2. Phone number")
        choice = input("Your choice (1/2): ").strip()
        
        try:
            if choice == '1':
                new_name = input("Enter new first name: ").strip()
                self.cur.execute(
                    "UPDATE phonebook SET first_name = %s WHERE phone = %s",
                    (new_name, phone)
                )
            elif choice == '2':
                new_phone = input("Enter new phone number: ").strip()
                self.cur.execute(
                    "UPDATE phonebook SET phone = %s WHERE phone = %s",
                    (new_phone, phone)
                )
            self.conn.commit()
            print("Contact updated successfully")
        except Exception as e:
            self.conn.rollback()
            print(f"Update error: {e}")

    def query_contacts(self):
        """Search contacts with filters"""
        print("\nSearch options:")
        print("1. By name")
        print("2. By phone")
        print("3. Show all")
        choice = input("Your choice (1/2/3): ").strip()
        
        try:
            if choice == '1':
                name = input("Enter name: ").strip()
                self.cur.execute(
                    "SELECT * FROM phonebook WHERE first_name ILIKE %s OR last_name ILIKE %s",
                    (f'%{name}%', f'%{name}%')
                )
            elif choice == '2':
                phone = input("Enter phone: ").strip()
                self.cur.execute(
                    "SELECT * FROM phonebook WHERE phone LIKE %s",
                    (f'%{phone}%',)
                )
            elif choice == '3':
                self.cur.execute("SELECT * FROM phonebook")
            
            results = self.cur.fetchall()
            if not results:
                print("No contacts found")
                return
            
            print("\nSearch results:")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")
        except Exception as e:
            print(f"Search error: {e}")

    def delete_contact(self):
        """Delete contact by name or phone"""
        print("\nDelete by:")
        print("1. First name")
        print("2. Phone number")
        choice = input("Your choice (1/2): ").strip()
        
        try:
            if choice == '1':
                name = input("Enter first name: ").strip()
                self.cur.execute(
                    "DELETE FROM phonebook WHERE first_name = %s",
                    (name,)
                )
            elif choice == '2':
                phone = input("Enter phone: ").strip()
                self.cur.execute(
                    "DELETE FROM phonebook WHERE phone = %s",
                    (phone,)
                )
            self.conn.commit()
            print(f"Deleted {self.cur.rowcount} contact(s)")
        except Exception as e:
            self.conn.rollback()
            print(f"Delete error: {e}")

    def close(self):
        """Close database connection"""
        self.cur.close()
        self.conn.close()