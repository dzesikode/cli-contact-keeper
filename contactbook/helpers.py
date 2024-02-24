#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tabulate import tabulate
from config import SESSION, URI
from contactbook.models import Base, Contact
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy_utils import database_exists, create_database


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


def add_contact(answers: dict) -> Contact:
    """
    Save a new contact to the database.
    """
    try:
        new_contact = Contact(**answers)
        session.add(new_contact)
        session.commit()
        print("New contact successfully added.")
        return new_contact
    except Exception as e:
        print(f"{e} An unexpected error occured.")


def view_all_entries() -> list[str]:
    """
    Views all entries within the database, along with headers.
    """
    entries = session.query(Contact).order_by(Contact.last_name).all()
    display_contacts(entries)


def search_contacts(query: str) -> None:
    """
    Searches contacts and displays the results.
    """
    results = (
        session.query(Contact)
        .filter(
            or_(
                (Contact.last_name.ilike(f"%{query}%")),
                (Contact.first_name.ilike(f"%{query}%")),
            )
        )
        .all()
    )
    return display_contacts(results)


def delete_contact(contact_id: int) -> None:
    """
    Removes the specified contact from the database.
    """
    try:
        contact = session.get(Contact, contact_id)
        session.delete(contact)
        session.commit()
        print("Contact successfully deleted.")
    except Exception as e:
        print(f"Failed to delete contact: {e}")


def update_contact(updated_fields: dict) -> Contact:
    """
    Updates contact information.
    """
    id = updated_fields.pop("id")
    contact = session.get(Contact, id)
    try:
        for key, value in updated_fields.items():
            if value:
                setattr(contact, key, value)
        session.commit()
        print("Contact successfully updated.")
        return contact
    except Exception as e:
        print(f"Failed to update contact: {e}")


def display_contacts(contacts: list[Contact]) -> list[str]:
    """
    Displays the contacts when viewing all or when searching for a contact.
    """
    HEADERS = [
        "#",
        "First Name",
        "Last Name",
        "Email",
        "Phone",
        "Line 1",
        "Line 2",
        "City",
        "State",
        "ZIP",
        "Country",
    ]

    rows = []
    if not contacts:
        print("No results found.\n")
        return rows
    for contact in contacts:
        rows.append(contact.__repr__())
    print(tabulate(rows, HEADERS, "fancy_grid"), end="\n")
    return rows
