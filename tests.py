from sqlalchemy_utils import drop_database
from config import DB_NAME, SESSION, URI
import pytest
from contactbook.database import db_connect, session

from contactbook.models import Contact


def generate_contact_data(**kwargs) -> dict:
    """Generate contact data for testing."""
    data = dict(
        first_name="John",
        last_name="Doe",
        email="jdoe@email.com",
        phone_number="123-456-7890",
        address_line_1="123 Main St.",
        address_line_2="",
        city="Pytest",
        state="AL",
        zipcode="12345",
        country="USA",
    )
    return {**data, **kwargs}


@pytest.fixture
def create_contact() -> Contact:
    def wrapper(**kwargs) -> Contact:
        data = generate_contact_data(**kwargs)
        return Contact.create(data)

    return wrapper


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session_ = db_connect()
    SESSION["session"] = session_
    yield
    session().close()
    drop_database(URI)
    print(f"Deleting database {DB_NAME}")


def test_add_contact():
    """Ensure a contact is properly saved to the db."""
    data = generate_contact_data()

    Contact.create(data)

    results = Contact.get_all()
    assert len(results) == 1
    result_dict = results[0].to_dict()
    assert result_dict.pop("id", None)
    assert result_dict == data


def test_update_contact(create_contact):
    """Ensure a contact is properly updated."""
    old_address = "900 Pytest Lane"
    new_address = "5675 Forest Road"

    contact: Contact = create_contact(address_line_1=old_address)
    assert contact.address_line_1 == old_address

    contact.update({"address_line_1": new_address})

    contacts = Contact.get_all()
    assert len(contacts) == 1
    contact_fields = contacts[0].to_dict()
    assert contact_fields == {**contact.to_dict(), "address_line_1": new_address}


def test_delete_contact(create_contact):
    """Ensure a contact is properly deleted."""
    contact_1: Contact = create_contact()
    contact_2: Contact = create_contact()

    contact_1.delete()

    contacts = Contact.get_all()
    assert len(contacts) == 1
    assert contacts[0].id == contact_2.id
