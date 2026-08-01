import streamlit as st

from solutions.src.main import ContactBook

st.title('Contact Book')

st.image('https://cdn-icons-png.flaticon.com/512/5765/5765132.png')

if "contact_book" not in st.session_state:
    st.session_state.contact_book = ContactBook()

contact_book = st.session_state.contact_book

user_choice = st.selectbox('Your choice:', ("1. Add Contact", "2. View Contacts", "3. Edit Contact", "4. Delete Contact", "5. Exit"))

if user_choice == '1. Add Contact':

    contact_name = st.text_input('Enter contact name:')
    contact_email = st.text_input('Enter contact email:')
    contact_phone = st.text_input('Enter contact phone number:')

    if st.button('Add Contact'):
        if contact_name in contact_book.contacts.keys():
            st.warning('This contact already exists.')
        elif contact_name and contact_email and contact_phone:
            contact_book.add_contact(contact_name, contact_email, contact_phone)
            st.success('Contact added successfully.')
        else:
            st.warning('Please fill all fields.')

elif user_choice == '2. View Contacts':
    if not contact_book.contacts:
        st.write("There are no contacts yet.")
    else:
        for name, info in contact_book.contacts.items():
            st.write("-----------------------")
            st.write("name:", name)
            st.write("phone:", info['phone'])
            st.write("email:", info['email'])
            st.write("-----------------------")

elif user_choice == '3. Edit Contact':
    selected_contact = st.text_input(f'Choose one of these contacts {contact_book.contacts.keys()}:')
    if selected_contact not in contact_book.contacts.keys():
        st.write('This contact does not exist in your contact book.')
    else:
        new_name = st.text_input(f"Enter new name for {selected_contact} or press Enter to keep unchanged: ")
        new_email = st.text_input("Enter new/updated email or press Enter to keep unchanged: ")
        new_phone = st.text_input("Enter new/updated phone number or press Enter to keep unchanged: ")

        if st.button('Edit'):
            if new_name in contact_book.contacts.keys():
                st.warning('This name already exists, please choose another one.')
            else:
                contact_book.edit_contact(selected_contact, new_name, new_phone, new_email)
                st.success('Contact updated successfully.')

elif user_choice == '4. Delete Contact':
    selected_contact = st.text_input(f'Choose one of these contacts {contact_book.contacts.keys()}:')
    if selected_contact not in contact_book.contacts.keys():
        st.write('This contact does not exist in your contact book.')
    else:
        if st.button('Delete'):
            if selected_contact not in contact_book.contacts.keys():
                st.write('This contact does not exist.')
            else:
                contact_book.remove_contact(selected_contact)
                st.success('Contact deleted.')

elif user_choice == '5. Exit':
    st.title('Thanks for using our app, goodbye!')
    st.image('https://img.magnific.com/free-vector/hand-drawn-farewell-lettering-background_23-2150019139.jpg?semt=ais_hybrid&w=740&q=80')