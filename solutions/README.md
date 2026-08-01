# Contact Book

A simple command-line (CLI) application written in Python for managing a list of contacts.

## Features
- Add a new contact (name, email, phone number)
- View the list of all contacts
- Edit a contact (update name, phone number, or email)
- Delete a contact
- Exit the program

## Requirements

- Python 3

No external libraries are required — the project only uses the Python standard library.

## Usage
```bash
python3 contact_book.py
```

Once started, the following menu is displayed:

```
===== Contact Book =====
1.Add Contact
2.View Contacts
3.Edit Contact
4.Delete Contact
5.Exit
```

Simply enter the number corresponding to the option you want.



## Menu Options

**1. Add Contact**
Prompts for a name, email, and phone number. The phone number must contain digits only, otherwise you'll be asked to re-enter it. If the name already exists, you'll be asked to enter a different one.

**2. View Contacts**
Displays every stored contact along with its email and phone number. If there are no contacts, an appropriate message is shown.

**3. Edit Contact**
First, select the contact you want to edit from the list (or type `q` to cancel). Then you can enter a new name, phone number, and/or email — leaving a field empty (just pressing Enter) keeps its current value.

**4. Delete Contact**
Select a contact from the list to remove it. Type `q` to cancel.

**5. Exit**
Closes the program.

## Known Limitations

- Contacts are stored in memory only and are lost when the program closes (no persistent storage, e.g. a JSON file, is implemented yet).
- Email addresses are not validated.
- The code is intentionally simple and intended for learning purposes / small projects, not for production use.

## License

Feel free to use, modify, and distribute this project as you like.

## 👤 Author

**Amir Hossein Pashmakian**
- Email : pashmakiana@gmail.com
- LinkedIn: https://www.linkedin.com/in/amirhossein-pashmakian-645909415/
- GitHub: https://github.com/pashmakiana-cell