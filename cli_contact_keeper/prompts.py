from PyInquirer import prompt
from cli_contact_keeper.helpers import search_contacts

from cli_contact_keeper.models import Contact

MAIN_MENU = [
    "Add a new contact",
    "Delete a contact",
    "Search the address book",
    "Update contact info",
    "View all entries",
    "Exit",
]


def contact_field_prompts() -> dict:
    """Displays prompts necessary for adding or updating a contact. Returns the field names and values."""
    prompts = []
    for field in Contact.get_fields():
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
            "message": "CLI Contact Keeper",
            "choices": MAIN_MENU,
        }
    ]
    selection = prompt(start_menu_prompt)["start_menu"]
    return selection


def update_contact_prompt(contacts: list[list[str]]) -> dict:
    """Prompt for updating of contacts"""
    update_prompt = [
        {
            "type": "list",
            "name": "choose_update",
            "message": "Choose the contact that you wish to update (press Enter to skip the field and keep current data):",
            "choices": [f"{contact[0]}  {contact[1]} {contact[2]}" for contact in contacts],
        },
    ]
    contact_name: str = prompt(update_prompt)["choose_update"]
    update_id = contact_name.split(" ")[0]

    updated_fields = contact_field_prompts()
    updated_fields["id"] = update_id
    return updated_fields


def delete_confirmation_prompt(contact_name: str) -> bool:
    """Prompt that confirms a deletion action."""
    delete_confirmation = [
        {
            "type": "confirm",
            "message": f"Are you sure you want to delete {contact_name}?",
            "name": "delete_contact",
            "default": False,
        }
    ]

    return prompt(delete_confirmation)["delete_contact"]


def delete_contact_prompt(contacts: list[list[str]]) -> int:
    """Prompt for the deletion of a contact, if there is more than one found in the search results."""
    delete_prompt = [
        {
            "type": "list",
            "name": "choose_delete",
            "message": "Choose the contact that you wish to delete:",
            "choices": [f"{contact[0]}  {contact[1]} {contact[2]}" for contact in contacts],
        },
    ]
    contact: str = prompt(delete_prompt)["choose_delete"]
    if contact:
        contact = contact.split()
        delete_id = contact.pop(0)
        name = " ".join(contact)

        delete_confirmed = delete_confirmation_prompt(name)
        if delete_confirmed:
            return int(delete_id)


def update_menu() -> None:
    """Starts the update menu."""
    while True:
        query = search_prompt()
        results = search_contacts(query)
        if results:
            updated_fields = update_contact_prompt(results)
            contact = Contact.get(updated_fields["id"])
            updated_fields = {
                k: updated_fields[k] for k in updated_fields if updated_fields[k]
            }
            contact.update(updated_fields)
        selection = menu_prompt("Update")
        if selection.startswith("Return"):
            break
        elif selection.startswith("Exit"):
            exit()
        continue


def search_menu() -> None:
    """Starts the search menu."""
    while True:
        query = search_prompt()
        search_contacts(query)
        selection = menu_prompt("Search for")
        if selection.startswith("Return"):
            break
        elif selection.startswith("Exit"):
            exit()
        continue


def delete_menu() -> None:
    """Starts the delete menu."""
    while True:
        query = search_prompt()
        results = search_contacts(query)
        if results:
            id = delete_contact_prompt(results)
            contact = Contact.get(id)
            contact.delete()
        selection = menu_prompt("Delete")
        if selection.startswith("Return"):
            break
        elif selection.startswith("Exit"):
            exit()
        continue


def add_menu() -> None:
    """Starts the add menu."""
    while True:
        new_contact_data = contact_field_prompts()
        Contact.create(new_contact_data)
        selection = menu_prompt("Add")
        if selection.startswith("Return"):
            break
        elif selection.startswith("Exit"):
            exit()
        continue
