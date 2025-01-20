from http import client
import faker
from app.users.schemas import SUserRegister
import pytest
from faker import Faker
from app.users.router import register_user

@pytest.fixture
def fake_user_data():
    return SUserRegister(
        name=fake.first_name(),
        surname=fake.last_name(),
        email=fake.email(),
        password=fake.password()
    )


