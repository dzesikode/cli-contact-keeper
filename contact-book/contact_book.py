from helpers import *
from view import menu_prompt, start_menu_prompt


if __name__ == '__main__':
    selection = start_menu_prompt()

    session = db_connect()

    # Add a new contact
    if selection.startswith("Add"):
        while True:
            add_contact()
            selection = menu_prompt("Add")
            if selection.startswith("Return"):
                pass
                break
            else:
                continue

    # Delete a contact
    elif selection.startswith("Delete"):
        while True:
            delete_contact()
            selection = menu_prompt("Delete")
            if selection.startswith("Return"):
                pass
                break
            else:
                continue

    # Search the contact book
    elif selection.startswith("Search"):
        while True:
            search_results()
            selection = menu_prompt("Search for")
            if selection.startswith("Return"):
                pass
                break
            else:
                continue


    # Update contact information
    elif selection.startswith("Update"):
        while True:
            update_contact()
            selection = menu_prompt("Update")
            if selection.startswith("Return"):
                pass
                break
            else:
                continue

    # View all entries
    elif selection.startswith("View"):
        view_all_entries()

    # Exit the program.
    elif selection.startswith("Exit"):
        exit()
