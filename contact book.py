# Initialize an empty dictionary to store contacts
contact_book = {}

# Function to add a contact
def add_contact(name, phone):
    if name in contact_book:
        print(f"{name} is already in your contact book.")
    else:
        contact_book[name] = phone
        print(f"Contact {name} has been added.")

# Function to view all contacts
def view_contacts():
    if contact_book:
        print("\nYour Contacts:")
        for name, phone in contact_book.items():
            print(f"Name: {name}, Phone: {phone}")
    else:
        print("\nYour contact book is empty.")

# Function to search for a contact
def search_contact(name):
    if name in contact_book:
        print(f"Name: {name}, Phone: {contact_book[name]}")
    else:
        print(f"{name} not found in your contact book.")

# Function to delete a contact
def delete_contact(name):
    if name in contact_book:
        del contact_book[name]
        print(f"Contact {name} has been deleted.")
    else:
        print(f"{name} not found in your contact book.")

# Main program loop
while True:
    print("\nOptions: 1. Add Contact  2. View Contacts  3. Search Contact  4. Delete Contact  5. Quit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        name = input("Enter contact name: ")
        phone = input("Enter contact phone number: ")
        add_contact(name, phone)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter the name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter the name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please choose again.")
