from sqlalchemy import Column, Integer, String, JSON

from app.database import Base

class Products(Base):
    __tablename__ = "products"

    product_id = Column(Integer, primary_key = True)
    name = Column(String, nullable= False)
    price = Column(Integer, nullable= False)
    quantity = Column(Integer)
    description = Column(String)
    stars = Column(Integer)
    ingredients = Column(String, nullable= False)
    nutrition = Column(String, nullable= False)
    image_id = Column(Integer)