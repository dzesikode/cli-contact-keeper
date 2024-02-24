from PyInquirer import prompt
from contactbook.helpers import (
    add_contact,
    delete_contact,
    search_contacts,
    update_contact,
)

from contactbook.models import Contact

MAIN_MENU = [
    "Add a new contact",
    "Delete a contact",
    "Search the address book",
    "Update contact information",
    "View all entries",
    "Exit the program",
]


def contact_field_prompts() -> dict:
    """Displays prompts necessary for adding or updating a contact. Returns the field names and values."""
    prompts = []
    for field in Contact.fields:
        if field != "id":
            field_msg = field.replace("_", " ").title()
            contact_prompt = {
                "type": "input",
                "name": field,
                "message": f"{field_msg}:",
            }
            prompts.append(contact_prompt)
    return prompt(prompts)


def menu_prompt(option: str) -> str:
    """
    Secondary menu prompt. Displays after a user has completed an action.
    Returns the user's selection from the choices listed below.
    """
    menu_options = [
        f"{option} another contact",
        "Return to the main menu",
        "Exit the program",
    ]
    menu_prompt = [
        {
            "type": "list",
            "name": "menu_options",
            "message": "What do you want to do?",
            "choices": menu_options,
        }
    ]
    selection = prompt(menu_prompt)["menu_options"]
    return selection


def search_prompt() -> str:
    """
    Prompt that returns a search query for use with querying the database
    """
    search_field = [
        {
            "type": "input",
            "name": "search",
            "message": "Enter a search term: ",
        },
    ]
    search_query = prompt(search_field)["search"]
    return search_query


def start_menu_prompt() -> str:
    """
    Displays the first prompt the user sees when starting the program. Returns
    the user's selection from the choices listed below.
    """
    start_menu_prompt = [
        {
            "type": "list",
            "name": "start_menu",
            "message": "Contact Book",
            "choices": MAIN_MENU,
        }
    ]
    selection = prompt(start_menu_prompt)["start_menu"]
    return selection


def update_contact_prompt(contacts: list[str]) -> dict:
    """"""
    if len(contacts) > 1:
        update_prompt = [
            {
                "type": "list",
                "name": "choose_update",
                "message": "Choose the contact that you wish to update (press Enter to skip the field and keep current data):",
                "choices": contacts,
            },
        ]
        contact_name: str = prompt(update_prompt)["choose_update"]
        update_id = contact_name.split(" ")[0]
    else:
        update_id = contacts[0].split(" ")[0]

    updated_fields = contact_field_prompts()
    updated_fields["id"] = update_id
    return updated_fields


def delete_confirmation_prompt(contact_name: str) -> bool:
    delete_confirmation = [
        {
            "type": "confirm",
            "message": f"Are you sure you want to delete {contact_name} from"
            " the contact book?",
            "name": "delete_contact",
            "default": False,
        }
    ]

    return prompt(delete_confirmation)["delete_contact"]


def delete_contact_prompt(contacts: list[Contact]) -> int:
    delete_prompt = [
        {
            "type": "list",
            "name": "choose_delete",
            "message": "Choose the contact that you wish to delete:",
            "choices": contacts,
        },
    ]
    contact_name: list[str] = prompt(delete_prompt)["choose_delete"].split()

    delete_id = contact_name.pop(0)
    name = " ".join(contact_name)

    delete_confirmed = delete_confirmation_prompt(name)
    if delete_confirmed:
        return int(delete_id)


def update_menu():
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
        continue


def search_menu():
    while True:
        query = search_prompt()
        search_contacts(query)
        selection = menu_prompt("Search for")
        if selection.startswith("Return"):
            break
        elif selection.startswith("Exit"):
            exit()
        continue


def delete_menu():
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


def add_menu():
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
