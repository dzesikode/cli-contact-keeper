#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from tabulate import tabulate


def start_menu_prompt():
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

headers = ['#', 'First Name', 'Last Name', 'Email', 'Phone Number',
           'Address Line 1', 'Address Line 2', 'City', 'State', 'Zipcode',
           'Country']


def menu_prompt(option):
    menu_options = [" another contact", "Return to the main menu",
                    "Exit the program"]
    menu_prompt = [
        {
            'type': 'list',
            'name': 'menu_options',
            'message': 'What do you want to do?',
            'choices': [option + menu_options[0], menu_options[1],
                        menu_options[2]]
        }
    ]
    selection = prompt(menu_prompt)['menu_options']
    return selection


def print_list_func(instance, print_list):
    print_list.append([instance.id, instance.first_name,
                       instance.last_name, instance.email,
                       instance.phone_number,
                       instance.address_line_1,
                       instance.address_line_2,
                       instance.city, instance.state,
                       instance.zipcode, instance.country])
    return print_list
