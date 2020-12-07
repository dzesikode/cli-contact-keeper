#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from PyInquirer import prompt
from tabulate import tabulate


def start_menu_prompt():
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


def menu_prompt(option):
    """
    Secondary menu prompt. Displays after a user has completed an action.
    Returns the user's selection from the choices listed below.
    """
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
    """
    Takes in an instance and an empty list as arguments and returns a list of
    instance information. Used for display when searching the contact book or
    viewing all entries.
    """
    print_list.append([instance.id, instance.first_name,
                       instance.last_name, instance.email,
                       instance.phone_number,
                       instance.address_line_1,
                       instance.address_line_2,
                       instance.city, instance.state,
                       instance.zipcode, instance.country])
    return print_list
