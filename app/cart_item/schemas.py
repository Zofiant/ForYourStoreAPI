from pydantic import BaseModel

class SCartItem(BaseModel):

    cart_item_id : int
    cart_id : int
    product_id: int
    quantity : int 