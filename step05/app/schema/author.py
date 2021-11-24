from . common import ItemNotFoundError, ItemAlreadyExistsError, Pagination
from pydantic import BaseModel
from typing import List


class AuthorBase(BaseModel):
    # The author name is common throughout the schema
    author_name: str


class AuthorCreate(AuthorBase):
    # Nothing more is needed from author create
    pass


class Author(AuthorBase):
    # Matches database model
    author_id: int

    class Config:
        orm_mode = True


class AuthorBook(BaseModel):
    book_id: int
    title: str
    page_count: int
    price: float


class AuthorDetails(Author):
    books: List[AuthorBook]


class AuthorNotFoundError(ItemNotFoundError):
    author_id: int


class AuthorAlreadyExistsError(ItemAlreadyExistsError, AuthorCreate):
    pass


class Authors(BaseModel):
    authors: List[Author]
    pagination: Pagination
