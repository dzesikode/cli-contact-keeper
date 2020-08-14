from tabulate import tabulate


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

def print_header():
    """
    Prints the header for the UI when viewing a contact.
    """
    print('ID'.center(3), 'Last Name'.center(31), 'First Name'.center(20),
          'Phone Number'.center(20), 'Email'.center(30), 'Address Line 1'.center(30),
          'Address Line 2'.center(20), 'City'.center(20), 'State'.center(15),
          'ZIP'.center(10), 'Country'.center(20))
    # print(tabulate([['ID', 'Last Name', 'First Name',
    # 'Phone Number', 'Email', 'Address Line 1', 'Address Line 2',
    # 'City', 'State', 'ZIP', 'Country']]))


def print_all_info(instance):
    """
    Prints the contact data.
    """
    header = ['ID', 'Last Name', 'First Name',
    'Phone Number', 'Email', 'Address Line 1', 'Address Line 2',
    'City', 'State', 'ZIP', 'Country']
    print(str(instance.id).ljust(3) + ' | ' + instance.last_name.ljust(30) + ' | ' + instance.first_name.ljust(20) + ' | ' +
          instance.phone_number.ljust(20) + ' | ' + instance.email.ljust(30) + ' | ' +
          instance.address_line_1.ljust(30) + '  ' + instance.address_line_2.ljust(20) + '  ' +
          instance.city.ljust(20) + ', ' + instance.state.ljust(15) + '  ' + instance.zipcode.ljust(10) +
          '  ' + instance.country.ljust(20))
    # print(tabulate([["ID", "Last Name"],[str(instance.id), instance.last_name, instance.first_name,
    #                instance.phone_number, instance.email,
    #                instance.address_line_1, instance.address_line_2,
    #                instance.city, instance.state, instance.zipcode,
    #                instance.country]]))
