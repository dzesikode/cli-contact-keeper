from models import Base, Contact
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from PyInquirer import prompt
from view import print_all_info, print_header


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
    answers = prompt(contact_fields)
    print(answers)
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
    print(new_contact.first_name)
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
    search_prompt = prompt(search_field)
    search_query = search_prompt['search']
    return search_query


def view_all_entries():
    """
    Views all entries within the database, along with a header.
    """
    print_header()
    for instance in session.query(Contact).order_by(Contact.last_name):
        print_all_info(instance)


def search_results():
    """
    Displays results based on the search query, along with a header.
    """
    search_query = search_prompt()
    trunacted_results = []
    print_header()
    for instance in session.query(Contact).filter(
                     or_(
                     (Contact.last_name.ilike(f'%{search_query}%')),
                     (Contact.first_name.ilike(f'%{search_query}%'))
                )):
                    trunacted_results.append('ID#:' + str(instance.id) + ' ' +
                                             instance.first_name + ' ' +
                                             instance.last_name)
                    print_all_info(instance)
    return trunacted_results


def filter_id(name):
    filter_id = session.query(Contact).filter_by(id=int(name[4]))
    return filter_id


def delete_contact():
    """
    Removes the specified contact from the database.
    """
    trunacted_results = search_results()
    results = [
        {
            'type': 'list',
            'name': 'choose_delete',
            'message': 'Choose the contact that you wish to delete:',
            'choices': trunacted_results,
        },
    ]
    choice = prompt(results)
    name = choice['choose_delete']

    delete_confirmation = [
        {
            'type': 'confirm',
            'message': f'Are you sure you want to delete {name} from the contact book?',
            'name': 'delete_contact',
            'default': False,
        }
    ]
    confirmation = prompt(delete_confirmation)
    if confirmation['delete_contact'] == True:
        try:
            session.query(Contact).filter_by(id=int(name[4])).delete()
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
    trunacted_results = search_results()
    results = [
        {
            'type': 'list',
            'name': 'choose_update',
            'message': 'Choose the contact that you wish to update:',
            'choices': trunacted_results,
        },
    ]
    choice = prompt(results)
    name = choice['choose_update']
    update_choices = [
        {
            'type': 'list',
            'name': 'update',
            'message': 'What would you like to change?',
            'choices': ['Name', 'Phone Number', 'Email',
                        'Postal Address']
        }
    ]
    update_choice = prompt(update_choices)
    if update_choice['update'] == 'Name':
        new_first_name = input("Enter a new first name (Press Enter to keep current name) ")
        print(new_first_name)
        new_last_name = input("Enter a new last name (Press Enter to keep current name) ")
        print(new_last_name)
        if new_first_name:
            filter_id(name).update({"first_name": new_first_name})
        if new_last_name :
            filter_id(name).update({"last_name": new_last_name})
        session.commit()
    elif update_choice['update'] == 'Phone Number':
        new_phone_number = input("Enter a new phone number (Press Enter to keep current phone number) ")
        if new_phone_number:
            session.query(Contact).filter_by(
                                            id=int(name[4])).update(
                                            {"phone_number": new_phone_number})
        session.commit()
    elif update_choice['update'] == 'Email':
        new_email = input("Enter a new email (Press Enter to keep current email) ")
        if new_email:
            session.query(Contact).filter_by(
                                            id=int(name[4])).update(
                                            {"email": new_email})
        session.commit()
    elif update_choice['update'] == 'Postal Address':
        new_address = input("Enter a new email (Press Enter to keep current email) ")
        if new_email:
            session.query(Contact).filter_by(
                                            id=int(name[4])).update(
                                            {"email": new_email})
