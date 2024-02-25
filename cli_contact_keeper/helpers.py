#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tabulate import tabulate
from cli_contact_keeper.models import Contact
from sqlalchemy import or_


def view_all_entries() -> list[str]:
    """
    Views all entries within the database, along with headers.
    """
    contacts = Contact.get_all(order_by="last_name")
    display_contacts(contacts)


def search_contacts(query: str) -> None:
    """
    Searches contacts and displays the results.
    """
    results = Contact.search(
        or_(
            (Contact.last_name.ilike(f"%{query}%")),
            (Contact.first_name.ilike(f"%{query}%")),
        )
    )
    return display_contacts(results)


def get_headers() -> list[str]:
    """Return the headers used for the table to display contacts."""
    result = []
    fields = Contact.get_fields()
    for field in fields:
        if (
            field.startswith("last")
            or field.startswith("first")
            or field.startswith("phone")
        ):
            result.append(field.split("_")[0])
        elif field.startswith("address"):
            result.append(f"line_{field[-1]}")
        elif field == "zipcode":
            result.append("zip")
        else:
            result.append(field)
    return result


def display_contacts(contacts: list[Contact]) -> list[list[str]]:
    """
    Displays the contacts when viewing all or when searching for a contact.
    """

    headers = get_headers()

    rows = []
    if not contacts:
        print("No results found.\n")
        return rows
    for contact in contacts:
        rows.append(list(contact.to_dict().values()))
    print(tabulate(rows, headers, "fancy_grid"), end="\n")
    return rows
