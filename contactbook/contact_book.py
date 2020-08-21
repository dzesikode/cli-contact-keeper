#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from helpers import db_connect, add_contact, delete_contact, search_results, \
                    update_contact, view_all_entries
from view import menu_prompt, start_menu_prompt


if __name__ == '__main__':
    while True:
        selection = start_menu_prompt()

        session = db_connect()

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
