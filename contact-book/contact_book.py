from __future__ import print_function, unicode_literals
from sqlalchemy import or_, func
from PyInquirer import prompt, print_json
from models import Base, Contact
from helpers import db_connect, add_contact, search_prompt, view_all_entries
from view import print_header, print_all_info


if __name__ == '__main__':

    START_MENU_CHOICES = ['V', 'A', 'D', 'S', 'U', 'X']

    start_menu = ("[V] -- View all entries\n"
                  "[A] -- Add new contact\n"
                  "[D] -- Delete a contact\n"
                  "[S] -- Search the address book\n"
                  "[U] -- Update contact information\n"
                  "[X] -- Exit the program\n")

    print('---------------Contact Book---------------')
    print(start_menu)

    choice = input()

    session = db_connect()

    # View all entries
    if choice.upper() == 'V':
            print_header()
            view_all_entries()

    # Add a new contact
    elif choice.upper() == 'A':
        add_contact()
        while True:
            add_another = [
                {
                'type': 'confirm',
                'message': 'Would you like to add another contact?',
                'name': 'add_another',
                'default': True,
                },
            ]
            answer = prompt(add_another)
            if answer['add_another'] == False:
                break
            else:
                add_contact()

    # Delete a contact
    elif choice.upper() == 'D':
        search_query = search_prompt()

    # Search the contact book
    elif choice.upper() == 'S':
        search_query = search_prompt()
        print_header()
        for instance in session.query(Contact).filter(
                         or_(
                         (Contact.last_name.ilike(f'%{search_query}%')),
                         (Contact.first_name.ilike(f'%{search_query}%'))
                    )):
                        print_all_info(instance)

    # Update contact information
    elif choice == 'U':
        pass

    # Exit the program.
    elif choice == 'X':
        pass
