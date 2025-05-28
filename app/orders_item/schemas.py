from pydantic import BaseModel

class SOrderItem(BaseModel):
    order_item_id:int
    order_id:int
    product_id:int
    quantity:int


