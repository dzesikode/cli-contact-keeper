

def print_header():
    """
    Prints the header for the UI when viewing a contact.
    """
    print('ID'.center(3), 'Last Name'.center(31), 'First Name'.center(20),
          'Phone Number'.center(20), 'Email'.center(30), 'Address Line 1'.center(30),
          'Address Line 2'.center(20), 'City'.center(20), 'State'.center(15),
          'ZIP'.center(10), 'Country'.center(20))


def print_all_info(instance):
    """
    Prints the contact data.
    """
    print(str(instance.id).ljust(3) + ' | ' + instance.last_name.ljust(30) + ' | ' + instance.first_name.ljust(20) + ' | ' +
          instance.phone_number.ljust(20) + ' | ' + instance.email.ljust(30) + ' | ' +
          instance.address_line_1.ljust(30) + '  ' + instance.address_line_2.ljust(20) + '  ' +
          instance.city.ljust(20) + ', ' + instance.state.ljust(15) + '  ' + instance.zipcode.ljust(10) +
          '  ' + instance.country.ljust(20))
