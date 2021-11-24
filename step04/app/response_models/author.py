from . common import ItemNotFoundRM, PaginationRM
from pydantic import BaseModel
from typing import List


class AuthorBookRM(BaseModel):
    book_id: int
    name: str
    page_count: int
    price: float


class AuthorMetaRM(BaseModel):
    author_id: int
    author: str


class AuthorRM(AuthorMetaRM):
    books: List[AuthorBookRM]


class AuthorNotFoundRM(ItemNotFoundRM):
    author_id: int


class AuthorListRM(BaseModel):
    authors: List[AuthorMetaRM]
    pagination: PaginationRM
