import sys

IS_PYTEST = "pytest" in sys.modules
DB_NAME = "contact_book" if not IS_PYTEST else "test"
URI = f'sqlite:///{DB_NAME}.db'
SESSION = None