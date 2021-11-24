from pydantic import BaseModel
from typing import Optional


class ItemNotFoundError(BaseModel):
    message: Optional[str] = "Item not found."


class ItemAlreadyExistsError(BaseModel):
    message: Optional[str] = "Item already exists."


class Pagination(BaseModel):
    page_id: int
    page_size: int
    prev_page_id: Optional[int] = None
    next_page_id: Optional[int] = None
    items_on_page: int
    total_items: int
