from __future__ import print_function, unicode_literals
from sqlalchemy import or_
from PyInquirer import prompt
from models import Base, Contact
from helpers import *
from view import print_start_menu, print_all_info


if __name__ == '__main__':
    print_start_menu()

    choice = input()

    session = db_connect()

    # View all entries
    if choice.upper() == 'V':
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
        delete_contact()

    # Search the contact book
    elif choice.upper() == 'S':
        search_results()

    # Update contact information
    elif choice.upper() == 'U':
        update_contact()

    # Exit the program.
    elif choice == 'X':
        pass
