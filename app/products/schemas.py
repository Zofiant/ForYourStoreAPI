from pydantic import BaseModel


class SProduct(BaseModel):
    name : str
    price : int
    quantity : int
    ingredients : str 
    nutrition : str 
    description : str | None = None
    stars : int | None = None
    image_id : int | None = None


class SProductAdd(BaseModel):
    product_id: int
    quantity: int