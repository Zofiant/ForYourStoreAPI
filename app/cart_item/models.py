from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Time
from app.database import Base

    
class Cart_items(Base):
    __tablename__ = "cart_items"
    cart_item_id = Column(Integer, primary_key= True)
    cart_id = Column(ForeignKey("carts.cart_id"))
    product_id = Column(ForeignKey("products.product_id"))
    