#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tabulate import tabulate
from contactbook.database import session
from contactbook.models import Contact
from sqlalchemy import or_


def add_contact(answers: dict) -> Contact:
    """
    Save a new contact to the database.
    """
    try:
        new_contact = Contact(**answers)
        session().add(new_contact)
        session().commit()
        print("New contact successfully added.")
        return new_contact
    except Exception as e:
        print(f"{e} An unexpected error occured.")


def view_all_entries() -> list[str]:
    """
    Views all entries within the database, along with headers.
    """
    entries = session().query(Contact).order_by(Contact.last_name).all()
    display_contacts(entries)


def search_contacts(query: str) -> None:
    """
    Searches contacts and displays the results.
    """
    results = (
        session()
        .query(Contact)
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
        contact = session().get(Contact, contact_id)
        session().delete(contact)
        session().commit()
        print("Contact successfully deleted.")
    except Exception as e:
        print(f"Failed to delete contact: {e}")


def update_contact(updated_fields: dict) -> Contact:
    """
    Updates contact information.
    """
    id = updated_fields.pop("id")
    contact = session().get(Contact, id)
    try:
        for key, value in updated_fields.items():
            if value:
                setattr(contact, key, value)
        session().commit()
        print("Contact successfully updated.")
        return contact
    except Exception as e:
        print(f"Failed to update contact: {e}")


def get_headers(contact: Contact) -> list[str]:
    result = []
    headers = contact.__table__.columns.keys()
    for header in headers:
        if (
            header.startswith("last")
            or header.startswith("first")
            or header.startswith("phone")
        ):
            result.append(header.split("_")[0])
        elif header.startswith("address"):
            result.append(f"line_{header[-1]}")
        elif header == "zipcode":
            result.append("zip")
        else:
            result.append(header)
    return result


def display_contacts(contacts: list[Contact]) -> list[str]:
    """
    Displays the contacts when viewing all or when searching for a contact.
    """

    headers = get_headers(contacts[0])

    rows = []
    if not contacts:
        print("No results found.\n")
        return rows
    for contact in contacts:
        rows.append(contact.to_dict().values())
    print(tabulate(rows, headers, "fancy_grid"), end="\n")
    return rows
