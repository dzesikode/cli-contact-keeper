#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from tabulate import tabulate

from contactbook.models import Contact


# A list of prompts used when adding a new contact or updating one.
CONTACT_FIELDS = [
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

# Headers which display above the list of contacts in the search function or
# when viewing all entries.
HEADERS = ['#', 'First Name', 'Last Name', 'Email', 'Phone Number',
           'Address Line 1', 'Address Line 2', 'City', 'State', 'Zipcode',
           'Country']


#TODO combine print_list_func and display_results?
def print_list_func(instance: Contact, print_list: list[str]) -> list[str]:
    """
    Returns a list of instance information. Used for display when querying the
    contact book or viewing all entries.
    
    """
    print_list.append([instance.id, instance.first_name, instance.last_name,
                       instance.email, instance.phone_number,
                       instance.address_line_1, instance.address_line_2,
                       instance.city, instance.state, instance.zipcode,
                       instance.country])
    return print_list


def display_results(print_list, headers=HEADERS, tablefmt='fancy_grid') -> list[str]:
    """
    Displays the contacts when viewing all or when searching for a contact.

    Keyword arguments:
    print_list: The list of contacts to be displayed
    headers: The headers to be displayed above the contact(s) (default HEADERS)
    tablefmt: How the table should be formatted with tabulate (default fancy_grid)
    """
    print(tabulate(print_list, headers, tablefmt), end='\n')
    return print_list
