from models import Base, Contact
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from PyInquirer import prompt
from view import contact_fields, headers
from tabulate import tabulate


def db_connect():
    """
    Connect to the sqlite database.
    """
    # Connect to the engine.
    engine = create_engine('sqlite:///contact_book.db', echo=False)

    # Create a schema
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    Session.configure(bind=engine)

    # Instantiate when you need to connect with the database
    session = Session()

    return session
session = db_connect()



def add_contact():
    """
    Save a new contact to the database.
    """
    answers = prompt(contact_fields)
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
    session.add(new_contact)
    session.commit()


def search_prompt():
    """
    Prompt that returns a search query for use with querying the database
    """
    search_field = [
        {
        'type': 'input',
        'name': 'search',
        'message': 'Enter a name: ',
        },
    ]
    search_query = prompt(search_field)['search']
    return search_query


def view_all_entries():
    """
    Views all entries within the database, along with headers.
    """
    print_list = []
    for instance in session.query(Contact).order_by(Contact.last_name):
        print_list.append([instance.first_name, instance.last_name,
                           instance.email, instance.phone_number,
                           instance.address_line_1, instance.address_line_2,
                           instance.city, instance.state, instance.zipcode,
                           instance.country])
    print(tabulate(print_list, headers=headers))


def search_results():
    """
    Displays results based on the search query, along with a header.
    """
    search_query = search_prompt()
    print_list = []
    for instance in session.query(Contact).filter(
                     or_(
                     (Contact.last_name.ilike(f'%{search_query}%')),
                     (Contact.first_name.ilike(f'%{search_query}%'))
                )):
                    print_list.append([instance.id, instance.first_name,
                                       instance.last_name, instance.email,
                                       instance.phone_number,
                                       instance.address_line_1,
                                       instance.address_line_2,
                                       instance.city, instance.state,
                                       instance.zipcode, instance.country])

    print(tabulate(print_list, headers=headers))
    return print_list


def delete_contact():
    """
    Removes the specified contact from the database.
    """
    print_list = search_results()

    # Create a list showing just the first and last name for each contact from
    # the search results
    name_list = [f"{i[1]} {i[2]}" for i in print_list]

    results = [
        {
            'type': 'list',
            'name': 'choose_delete',
            'message': 'Choose the contact that you wish to delete:',
            'choices': name_list,
        },
    ]
    # Get the first and last name from the user's choice
    delete_first_name, delete_last_name = prompt(results)['choose_delete'].split()

    delete_confirmation = [
        {
            'type': 'confirm',
            'message': f'Are you sure you want to delete {delete_first_name} {delete_last_name} from the contact book?',
            'name': 'delete_contact',
            'default': False,
        }
    ]
    if prompt(delete_confirmation)['delete_contact'] == True:
        try:
            session.query(Contact).filter_by(first_name=delete_first_name,
                                             last_name=delete_last_name).delete()
            session.commit()
            print("Contact successfully deleted.")
        except Exception:
            print("An error occured.")
    else:
        print("Operation cancelled.")


def update_contact():
    """
    Updates contact information.
    """
    print_list = search_results()

    # Create a list showing just the first and last name for each contact from
    # the search results
    name_list = [f"{i[1]} {i[2]}" for i in print_list]
    results = [
        {
            'type': 'list',
            'name': 'choose_update',
            'message': 'Choose the contact that you wish to update (press Enter to keep current data):',
            'choices': name_list
        },
    ]

    # Get the first and last name from the user's choice
    update_first_name, update_last_name = prompt(results)['choose_update'].split()

    updates = prompt(contact_fields)

    # Commit any filled-in fields to the database
    for k, v in updates.items():
        if v:
            session.query(Contact).filter_by(first_name=update_first_name,
                                             last_name=update_last_name).update({k:v})
    session.commit()
