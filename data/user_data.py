from faker import Faker
from models.user import User
from utils.config import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
fake = Faker()

def create_user(name=None, last_name=None,email = None,password = None):
    return User(
        name if name is not None else fake.first_name(),
        last_name if last_name is not None else fake.last_name(),
        email if email is not None else fake.unique.email(),
        password if password is not None else fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )

def existing_user():
    return create_user(
        name="Anna",
        last_name="Sky",
        email=EXISTING_USER_EMAIL,
        password=EXISTING_USER_PASSWORD
    )
