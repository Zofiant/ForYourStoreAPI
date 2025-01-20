import enum
from sqlalchemy import Column, Integer, String, JSON, Enum
from sqlalchemy.dialects.postgresql import ENUM

from app.database import Base
    
class User_role(enum.Enum):
    user= "User"
    seller= "Seller"
    admin= "Admin"
class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    surname = Column(String, nullable= False)
    email = Column(String, nullable= False,unique=True)
    password = Column(String, nullable= False)
    role = Column(Enum(User_role))
    image_id = Column(Integer)
    
