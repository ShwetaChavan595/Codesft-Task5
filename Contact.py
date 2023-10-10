# Initialize an empty contact book
contact_book = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contact_book[name] = {'Phone': phone, 'Email': email}
    print(f"{name} has been added to the contact book.")

# Function to search for a contact
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contact_book:
        print(f"Name: {name}")
        print(f"Phone: {contact_book[name]['Phone']}")
        print(f"Email: {contact_book[name]['Email']}")
    else:
        print(f"{name} not found in the contact book.")

# Function to display all contacts
def display_contacts():
    if contact_book:
        print("Contacts:")
        for name, info in contact_book.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print("-" * 20)
    else:
        print("The contact book is empty.")

# Main menu loop
while True:
    print("\nContact Book Menu:")
    print("1. Add a Contact")
    print("2. Search for a Contact")
    print("3. Display All Contacts")
    print("4. Quit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        display_contacts()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
