

def print_start_menu():
    START_MENU_CHOICES = ['V', 'A', 'D', 'S', 'U', 'X']

    start_menu = ("[V] -- View all entries\n"
                  "[A] -- Add new contact\n"
                  "[D] -- Delete a contact\n"
                  "[S] -- Search the address book\n"
                  "[U] -- Update contact information\n"
                  "[X] -- Exit the program\n")

    print('---------------Contact Book---------------')
    print(start_menu)

contact_fields = [
    {
    'type': 'input',
    'name': 'first_name',
    'message': 'First Name: ',
    },
    {
    'type': 'input',
    'name': 'last_name',
    'message': 'Last Name: ',
    },
    {
    'type': 'input',
    'name': 'email',
    'message': 'Email Address: ',
    },
    {
    'type': 'input',
    'name': 'phone_number',
    'message': 'Phone Number: ',
    },
    {
    'type': 'input',
    'name': 'address_line_1',
    'message': 'Address Line 1: ',
    },
    {
    'type': 'input',
    'name': 'address_line_2',
    'message': 'Address Line 2: ',
    },
    {
    'type': 'input',
    'name': 'city',
    'message': 'City: ',
    },
    {
    'type': 'input',
    'name': 'state',
    'message': 'State: ',
    },
    {
    'type': 'input',
    'name': 'zipcode',
    'message': 'Zipcode: ',
    },
    {
    'type': 'input',
    'name': 'country',
    'message': 'Country: ',
    },
]

headers = ['ID', 'Last Name', 'First Name', 'Email', 'Phone Number',
           'Address Line 1', 'Address Line 2', 'City', 'State', 'Zipcode',
           'Country']
