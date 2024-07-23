class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts):
                print(f"Contact {index + 1}:\n{contact}")

    def search_contacts(self, search_term):
        search_results = []
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                search_results.append(contact)
        return search_results

    def update_contact(self, name, phone_number, email, address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = phone_number
                contact.email = email
                contact.address = address
                print(f"Contact '{name}' updated successfully.")
                return
        print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")


def main():
    contact_manager = ContactManager()

    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n===== Add Contact =====")
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone_number, email, address)
            contact_manager.add_contact(new_contact)
            print("Contact added successfully.")

        elif choice == "2":
            print("\n===== View Contacts =====")
            contact_manager.view_contacts()

        elif choice == "3":
            print("\n===== Search Contact =====")
            search_term = input("Enter name or phone number to search: ")
            search_results = contact_manager.search_contacts(search_term)
            if search_results:
                print("\nSearch results:")
                for contact in search_results:
                    print(contact)
            else:
                print("No matching contacts found.")

        elif choice == "4":
            print("\n===== Update Contact =====")
            name = input("Enter the name of the contact to update: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            contact_manager.update_contact(name, phone_number, email, address)

        elif choice == "5":
            print("\n===== Delete Contact =====")
            name = input("Enter the name of the contact to delete: ")
            contact_manager.delete_contact(name)

        elif choice == "6":
            print("<Exiting>")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
