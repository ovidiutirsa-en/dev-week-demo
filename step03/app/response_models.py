from pydantic import BaseModel
from typing import List, Optional


class BookRM(BaseModel):
    book_id: int
    name: str
    author: str
    page_count: int
    price: float


class ItemNotFoundRM(BaseModel):
    message: Optional[str] = "Item not found"


class BookNotFoundRM(ItemNotFoundRM):
    book_id: int


class BookListRM(BaseModel):
    books: List[BookRM]
    total_count: int
    total_pages: int
    page_id: int
    page_size: int
    items_on_page: int
