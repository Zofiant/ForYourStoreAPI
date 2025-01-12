from pydantic import BaseModel


class SProduct(BaseModel):
    product_id : int 
    name : str
    price : int
    stars : int | None = None
    nutrition : str 
    description : str | None = None
    ingredients : str 
    image_id : int | None = None
