from tabulate import tabulate

class ContactBook:
    """
    A class used to represent a Contact Book.
    """

    def __init__(self):
        """
        Initialize contact book object with an empty dictionary.
        """
        self.contacts = {}

    def add_contact(self, name: str, email: str, phone: str):
        """
        Adds a new contact to the contact book.

        :param str name: The name of the contact
        :param str email: The email address of the contact
        :param str phone: The phone number of the contact
        """
        self.contacts[name] = {'email': email, 'phone': phone}

    def view_contacts(self):
        """
        Displays all contacts in the contact book.
        """
        if not self.contacts:
            print("There are no contacts yet.")
        else:
            table_data = [
                [name, info['phone'], info['email']]
                for name, info in self.contacts.items()
            ]
            print(tabulate(table_data, headers=['Name', 'Phone', 'Email'], tablefmt='grid'))
            
    def edit_contact(self, name: str, new_name=None, phone=None, email=None):
        """
        Edits an existing contact in the contact book.

        :param str name: The name of the contact to edit
        :param str new_name: The new name of the contact, keeps the old one if None
        :param str phone: The new phone number of the contact, keeps the old one if None
        :param str email: The new email address of the contact, keeps the old one if None
        """
        if new_name:
            # Move the contact to a new key and drop the old one
            self.contacts[new_name] = self.contacts.pop(name)
            # The key has changed, so use the new name for any further update below
            name = new_name

        if phone:
            self.contacts[name]['phone'] = phone
        if email:
            self.contacts[name]['email'] = email

    def remove_contact(self, name):
        """
        Deletes a contact from the contact book.
        :param str name: The name of the contact to delete
        """
        if name in self.contacts:
            self.contacts.pop(name)


def print_menu():
    """Prints the main menu of the program."""
    print("===== Contact Book =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    """
    Main loop of the program.
    Reads the user's choice and calls the matching method.
    """
    contact_book = ContactBook()
    while True:
        print_menu()
        user_choice = input('Enter your choice: ').strip()

        # ------- Add Contact -------
        if user_choice == "1":

            # Ask for a name that is not already taken
            while True:
                contact_name = input('Enter contact name: ').strip()
                if contact_name not in contact_book.contacts.keys():
                    break
                else:
                    print('This name already exists, please choose another one.')
                    continue

            contact_email = input('Enter contact email: ')

            # Ask for a phone number, only digits are accepted
            while True:
                contact_phone = input('Enter contact phone number: ')
                if contact_phone.isdigit():
                    break
                else:
                    print('Phone number must contain digits only.')
                    continue

            contact_book.add_contact(contact_name, contact_email, contact_phone)
            print("Contact added successfully.")

        # ------- View Contacts -------
        elif user_choice == "2":
            contact_book.view_contacts()

        # ------- Edit Contact -------
        elif user_choice == "3":

            # Pick a contact to edit
            while True:
                contact_name = input(
                    f"\nEnter the name of the contact to edit from {contact_book.contacts.keys()} (press q to exit): "
                ).strip()
                if contact_name == 'q':
                    break
                elif contact_name not in contact_book.contacts.keys():
                    print("This contact doesn't exist.")
                    continue
                else:
                    break

            if contact_name == 'q':
                continue  # back to the main menu

            # Ask for a new name (leave empty to keep the current one)
            while True:
                new_name = input(f"Enter new name for {contact_name} or press Enter to keep unchanged: ")
                if new_name == "" or new_name not in contact_book.contacts.keys():
                    break
                else:
                    print('This name already exists, please choose another one.')
                    continue

            # Ask for a new phone number
            # note: an empty value must also be accepted, it means "keep unchanged"
            while True:
                new_phone = input("Enter new/updated phone number or press Enter to keep unchanged: ")
                if new_phone == "" or new_phone.isdigit():
                    break
                else:
                    print('This phone number is not valid, please try again.')

            new_email = input("Enter new/updated email or press Enter to keep unchanged: ")

            contact_book.edit_contact(
                contact_name,
                new_name or None,
                new_phone or None,
                new_email or None
            )

        # ------- Delete Contact -------
        elif user_choice == "4":

            if not contact_book.contacts:
                print("There are no contacts yet.")
                continue

            while True:
                contact_name = input(
                    f"Choose one of these {contact_book.contacts.keys()} (press q to exit): "
                ).strip()
                if contact_name == 'q':
                    break
                elif contact_name not in contact_book.contacts.keys():
                    print('This name does not exist.')
                else:
                    break

            if contact_name != 'q':
                contact_book.remove_contact(contact_name)
                print('Contact deleted.')

        # ------- Exit -------
        elif user_choice == "5":
            break

        else:
            print('Invalid choice.')
            continue


if __name__ == "__main__":
    main()
