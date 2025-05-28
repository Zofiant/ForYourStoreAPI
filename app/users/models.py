import enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ENUM
from app.database import Base
    
class UserRole(enum.Enum):
    user= "User"
    seller= "Seller"
    admin= "Admin"

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role = Column(ENUM(UserRole, name="user_role"))  # Explicitly name the enum type
    image_id = Column(Integer)
    
