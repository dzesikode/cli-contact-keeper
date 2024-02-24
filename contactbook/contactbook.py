#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contactbook.helpers import (
    add_contact,
    delete_contact,
    search_contacts,
    update_contact,
    view_all_entries,
)
from contactbook.prompts import (
    delete_contact_prompt,
    menu_prompt,
    search_prompt,
    start_menu_prompt,
    contact_field_prompts,
    update_contact_prompt,
)


def start_menu() -> None:
    """Entry point for the program."""
    while True:
        selection = start_menu_prompt()

        # Add a new contact
        if selection.startswith("Add"):
            while True:
                new_contact_data = contact_field_prompts()
                add_contact(new_contact_data)
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
                query = search_prompt()
                results = search_contacts(query)
                id = delete_contact_prompt(results)
                delete_contact(id)
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
                query = search_prompt()
                search_contacts(query)
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
                query = search_prompt()
                results = search_contacts(query)
                updated_fields = update_contact_prompt(results)
                update_contact(updated_fields)
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


if __name__ == "__main__":
    start_menu()
