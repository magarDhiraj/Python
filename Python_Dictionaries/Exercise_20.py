# Exercise 20: Simple Contact Book
contacts = {
    "Ram": "9841000000",
    "Sita": "9851000000",
    "Hari": "9861000000"
}

while True:
    print("\n===== Contact Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added successfully.")

    elif choice == "2":
        name = input("Enter contact name to search: ")

        if name in contacts:
            print(name, "->", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Enter contact name to update: ")

        if name in contacts:
            phone = input("Enter new phone number: ")
            contacts[name] = phone
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("\nAll contacts:")
        if contacts:
            for name, phone in contacts.items():
                print(name, "->", phone)
        else:
            print("No contacts available.")

    elif choice == "6":
        print("Exiting contact book...")
        break

    else:
        print("Invalid choice. Please select 1-6.")
        