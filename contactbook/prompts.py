from PyInquirer import prompt


def menu_prompt(option: str) -> dict:
    """
    Secondary menu prompt. Displays after a user has completed an action.
    Returns the user's selection from the choices listed below.
    """
    menu_options = [f"{option} another contact", "Return to the main menu",
                    "Exit the program"]
    menu_prompt = [
        {
            'type': 'list',
            'name': 'menu_options',
            'message': 'What do you want to do?',
            'choices': menu_options
        }
    ]
    selection = prompt(menu_prompt)['menu_options']
    return selection


def search_prompt() -> str:
    """
    Prompt that returns a search query for use with querying the database
    """
    search_field = [
        {
            'type': 'input',
            'name': 'search',
            'message': 'Enter a search term: ',
        },
    ]
    search_query = prompt(search_field)['search']
    return search_query


def start_menu_prompt() -> dict:
    """
    Displays the first prompt the user sees when starting the program. Returns
    the user's selection from the choices listed below.
    """
    START_MENU_CHOICES = ['Add a new contact', 'Delete a contact',
                          'Search the address book',
                          'Update contact information', 'View all entries',
                          'Exit the program']
    start_menu_prompt = [
        {
            'type': 'list',
            'name': 'start_menu',
            'message': 'Contact Book',
            'choices': START_MENU_CHOICES
        }
    ]
    selection = prompt(start_menu_prompt)['start_menu']
    return selection