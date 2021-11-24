from . common import ItemNotFoundError, ItemAlreadyExistsError, Pagination
from pydantic import BaseModel
from typing import List


class BookBase(BaseModel):
    # Common attributes
    title: str
    page_count: int
    price: float


class BookCreate(BookBase):
    # Nothing more is needed from book create
    author_id: int


class Book(BookBase):
    # Matches database model
    book_id: int
    author_id: int

    class Config:
        orm_mode = True


class BookNotFoundError(ItemNotFoundError):
    book_id: int


class BookAlreadyExistsError(ItemAlreadyExistsError, BookCreate):
    pass


class Books(BaseModel):
    books: List[Book]
    pagination: Pagination
