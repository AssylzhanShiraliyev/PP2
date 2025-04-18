from phonebook import PhoneBook

def show_menu():
    """Display main menu options"""
    print("\nPhone Book Application")
    print("1. Import from CSV")
    print("2. Add contact manually")
    print("3. Update contact")
    print("4. Search contacts")
    print("5. Delete contact")
    print("6. Exit")

def main():
    pb = PhoneBook()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            filename = input("Enter CSV filename: ").strip()
            pb.insert_from_csv(filename)
        elif choice == '2':
            pb.insert_from_console()
        elif choice == '3':
            pb.update_contact()
        elif choice == '4':
            pb.query_contacts()
        elif choice == '5':
            pb.delete_contact()
        elif choice == '6':
            print("Exiting application...")
            break
        else:
            print("Invalid choice, please try again")
    
    pb.close()

if __name__ == "__main__":
    main()