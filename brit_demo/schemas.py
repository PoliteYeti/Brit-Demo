from pydantic import BaseModel


class Item(BaseModel):
    price: int
    description: str


class StoredItem(Item):
    id: int

    class Config:
        orm_mode = True


class Summary(BaseModel):
    totalcost: int
