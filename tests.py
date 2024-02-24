from sqlalchemy import select
from sqlalchemy_utils import drop_database
from config import DB_NAME, URI
from contactbook.helpers import db_connect
import pytest

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
    from contactbook.helpers import add_contact

    def wrapper(**kwargs) -> Contact:
        data = generate_contact_data(**kwargs)
        return add_contact(data)

    return wrapper


@pytest.fixture(autouse=True)
def setup_and_teardown():
    session = db_connect()
    yield
    session.close()
    drop_database(URI)
    print(f"Deleting database {DB_NAME}")


def test_add_contact():
    """Ensure a contact is properly saved to the db."""
    from contactbook.helpers import add_contact

    data = generate_contact_data()

    add_contact(data)

    results = db_connect().scalars(select(Contact)).all()
    assert len(results) == 1
    result_dict = results[0].to_dict()
    assert result_dict.pop("id", None)
    assert result_dict == data


def test_update_contact(create_contact):
    """Ensure a contact is properly updated."""
    from contactbook.helpers import update_contact

    old_address = "900 Pytest Lane"
    new_address = "5675 Forest Road"

    contact: Contact = create_contact(address_line_1=old_address)
    assert contact.address_line_1 == old_address

    update_contact({"id": contact.id, "address_line_1": new_address})

    contacts = db_connect().scalars(select(Contact)).all()
    assert len(contacts) == 1
    contact_fields = contacts[0].to_dict()
    assert contact_fields == {**contact.to_dict(), "address_line_1": new_address}


def test_delete_contact(create_contact):
    """Ensure a contact is properly deleted."""
    from contactbook.helpers import delete_contact

    contact_1, contact_2 = [create_contact(), create_contact()]

    delete_contact(contact_1.id)

    contacts = db_connect().scalars(select(Contact)).all()
    assert len(contacts) == 1
    assert contacts[0].id == contact_2.id
