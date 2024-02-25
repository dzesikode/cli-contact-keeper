#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from cli_contact_keeper.database import db_connect
from cli_contact_keeper.helpers import (
    view_all_entries,
)
from cli_contact_keeper.prompts import (
    add_menu,
    delete_menu,
    search_menu,
    start_menu_prompt,
    update_menu,
)
from config import SESSION


def start_menu() -> None:
    """Entry point for the program."""
    session = db_connect()
    SESSION["session"] = session
    while True:
        selection = start_menu_prompt()
        choice = selection.split()[0].lower()

        options = {
            "add": add_menu,
            "delete": delete_menu,
            "search": search_menu,
            "update": update_menu,
            "view": view_all_entries,
            "exit": exit,
        }

        options[choice]()


if __name__ == "__main__":
    start_menu()
