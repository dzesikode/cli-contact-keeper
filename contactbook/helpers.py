#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from config import SESSION, URI
from contactbook.models import Base, Contact
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker, Session
from PyInquirer import prompt
from sqlalchemy_utils import database_exists, create_database
from contactbook.view import print_list_func, display_results, CONTACT_FIELDS

def db_session() -> Session:
    return SESSION


def db_connect() -> Session:
    """
    Connect to the sqlite database.
    """
    engine = create_engine(URI, echo=False)

    if not database_exists(URI):
        create_database(URI)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    SESSION = Session()
    return SESSION



session = db_connect()


def add_contact() -> None:
    """
    Save a new contact to the database.
    """
    answers = prompt(CONTACT_FIELDS)
    new_contact = Contact(first_name=answers['first_name'],
                          last_name=answers['last_name'],
                          email=answers['email'],
                          phone_number=answers['phone_number'],
                          address_line_1=answers['address_line_1'],
                          address_line_2=answers['address_line_2'],
                          city=answers['city'],
                          state=answers['state'],
                          zipcode=answers['zipcode'],
                          country=answers['country'])
    try:
        session.add(new_contact)
        session.commit()
        print("New contact successfully added.")
    except Exception as e:
        print(f"{e} An unexpected error occured.")


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


def view_all_entries() -> list[str]:
    """
    Views all entries within the database, along with headers.
    """
    print_list = []
    for instance in session.query(Contact).order_by(Contact.last_name):
        print_list = print_list_func(instance, print_list)
    display_results(print_list)


def search_results() -> list[str]:
    """
    Displays results based on the search query, along with a header.
    """
    search_query = search_prompt()
    print_list = []
    for instance in session.query(Contact).filter(
                        or_(
                            (Contact.last_name.ilike(f'%{search_query}%')),
                            (Contact.first_name.ilike(f'%{search_query}%')))):
        print_list = print_list_func(instance, print_list)
    if print_list == []:
        print("No results found.\n")
    else:
        display_results(print_list)
    return print_list


def delete_contact() -> None:
    """
    Removes the specified contact from the database.
    """
    print_list = search_results()

    # Create a list showing just the id and first and last name for each
    # contact from the search results. The id is in case of duplicates.
    if print_list != []:
        name_list = [f"{i[0]}   {i[1]} {i[2]}" for i in print_list]

        delete_prompt = [
            {
                'type': 'list',
                'name': 'choose_delete',
                'message': 'Choose the contact that you wish to delete:',
                'choices': name_list,
            },
        ]
        results = prompt(delete_prompt)['choose_delete'].split()

        # Contact has more than two names and one id
        if len(results) > 3:
            delete_id = results[0]
            identifier = results[1:]

        # Contact has two names and one id
        elif len(results) == 3:
            delete_id, delete_firstname, delete_lastname = results
            identifier = delete_firstname + ' ' + delete_lastname

        # Contact has only one name and one id
        elif len(results) == 2:
            delete_id, delete_name = results
            identifier = delete_name

        # Contact has only an id as an identifier
        elif len(results) == 1:
            delete_id = results[0]
            identifier = delete_id

        # Get the first and last name from the user's choice
        delete_confirmation = [
            {
                'type': 'confirm',
                'message': f'Are you sure you want to delete {identifier} from'
                            ' the contact book?',
                'name': 'delete_contact',
                'default': False,
            }
        ]

        if prompt(delete_confirmation)['delete_contact'] is True:
            try:
                session.query(Contact).filter_by(id=delete_id).delete()
                session.commit()
                print("Contact successfully deleted.")
            except Exception:
                print("An unexpected error occured.")
        else:
            print("Operation cancelled.")
    else:
        pass


def update_contact() -> None:
    """
    Updates contact information.
    """
    print_list = search_results()
    if print_list != []:
        # Create a list showing just the first and last name for each contact
        # from the search results
        name_list = [f"{i[0]}   {i[1]} {i[2]}" for i in print_list]

        update_prompt = [
            {
                'type': 'list',
                'name': 'choose_update',
                'message': 'Choose the contact that you wish to update'
                           ' (press Enter to skip the field and keep current \
                            data):',
                'choices': name_list
            },
        ]
        results = prompt(update_prompt)['choose_update'].split()
        update_id = results[0]

        updates = prompt(CONTACT_FIELDS)

        # Commit any filled-in fields to the database
        for k, v in updates.items():
            if v:
                session.query(Contact).filter_by(id=update_id).update({k: v})
        session.commit()
        print("Contact successfully updated.")
    else:
        pass
