#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contactbook.helpers import add_contact, delete_contact, search_results, \
                    update_contact, view_all_entries
from contactbook.view import menu_prompt, start_menu_prompt


def start_menu():
    while True:
        selection = start_menu_prompt()

        # Add a new contact
        if selection.startswith("Add"):
            while True:
                add_contact()
                selection = menu_prompt("Add")
                if selection.startswith("Return"):
                    break
                elif selection.startswith("Exit"):
                    exit()
                else:
                    continue

        # Delete a contact
        elif selection.startswith("Delete"):
            while True:
                delete_contact()
                selection = menu_prompt("Delete")
                if selection.startswith("Return"):
                    break
                elif selection.startswith("Exit"):
                    exit()
                else:
                    continue

        # Search the contact book
        elif selection.startswith("Search"):
            while True:
                search_results()
                selection = menu_prompt("Search for")
                if selection.startswith("Return"):
                    break
                elif selection.startswith("Exit"):
                    exit()
                else:
                    continue

        # Update contact information
        elif selection.startswith("Update"):
            while True:
                update_contact()
                selection = menu_prompt("Update")
                if selection.startswith("Return"):
                    break
                elif selection.startswith("Exit"):
                    exit()
                else:
                    continue

        # View all entries
        elif selection.startswith("View"):
            view_all_entries()
            continue

        # Exit the program.
        elif selection.startswith("Exit"):
            exit()
            break


if __name__ == '__main__':
    start_menu()