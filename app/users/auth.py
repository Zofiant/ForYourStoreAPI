from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import SECRET_KEY, ALGORITHM
from app.users.repository import UserRepository

if not hasattr(bcrypt, '__about__'):
    bcrypt.__about__ = type('about', (object,), {'__version__': bcrypt.__version__})

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UserRepository.find_one_or_none(email = email)
    if not user:
        print("None user")
        return None
    if not verify_password(password, user.password):
        print("Wrong password")
        return None
    return user





