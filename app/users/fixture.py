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

def test_register_user_success(fake_user_data):
    response = client.post("/register", data=fake_user_data.dict(exclude_unset=True))
    assert response.status_code == 201
