# Contact Book Program

contacts = []

# Function to add contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


# Function to view all contacts
def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for contact in contacts:
            print("Name:", contact["name"], "| Phone:", contact["phone"])
        print()


# Function to search contact
def search_contact():
    search = input("Enter Name or Phone to search: ")
    found = False

    for contact in contacts:
        if search.lower() in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            found = True
            break

    if not found:
        print("Contact not found.\n")


# Function to update contact
def update_contact():
    name = input("Enter the name of contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("Enter new Phone Number: ")
            contact["email"] = input("Enter new Email: ")
            contact["address"] = input("Enter new Address: ")
            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


# Function to delete contact
def delete_contact():
    name = input("Enter the name of contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


# Main menu
while True:
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")
