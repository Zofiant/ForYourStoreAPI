from sqlalchemy import JSON, Column, Integer, String, ForeignKey, Time, Enum
from app.database import Base


class Order_items(Base):
    __tablename__ = "order_items"
    order_item_id = Column(Integer, primary_key= True)
    order_id = Column(ForeignKey("orders.order_id"))
    product_id = Column(ForeignKey("products.product_id"))
    quantity = Column(Integer)
    