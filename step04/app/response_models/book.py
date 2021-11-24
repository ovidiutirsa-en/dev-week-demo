from . common import ItemNotFoundRM, PaginationRM
from pydantic import BaseModel
from typing import List


class BookRM(BaseModel):
    book_id: int
    name: str
    author: str
    page_count: int
    price: float


class BookNotFoundRM(ItemNotFoundRM):
    book_id: int


class BookListRM(BaseModel):
    books: List[BookRM]
    pagination: PaginationRM
