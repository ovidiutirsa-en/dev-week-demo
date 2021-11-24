from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .utils import get_pagination_parameters
from ..dependencies import get_db
from ..schema import author as aus
from ..schema import book as bs
from ..services import author_handler as ah
from ..services import book_handler as bh


author_router = APIRouter()


@author_router.post(
    "/authors/",
    summary="Creates an author.",
    response_model=aus.Author,
    responses={status.HTTP_400_BAD_REQUEST: {"model": aus.AuthorAlreadyExistsError}},
    tags=["authors"],
)
def create_author_endpoint(author: aus.AuthorCreate, db: Session = Depends(get_db)):
    db_user = ah.get_author_by_name(db, author_name=author.author_name)
    if db_user:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"author_name": author.author_name, "message": "Author already exists."},
        )
    return ah.create_author(db, author)


@author_router.get(
    "/authors/",
    summary="Gets a list of authors.",
    response_model=aus.Authors,
    tags=["authors"],
)
async def get_authors_endpoint(page_id: int = 0, page_size: int = 5, db: Session = Depends(get_db)):
    authors = ah.get_authors(db, page_id, page_size)
    authors_count = ah.get_authors_count(db)

    return {
        "authors": authors,
        "pagination": get_pagination_parameters(page_id, page_size, len(authors), authors_count)
    }


@author_router.get(
    "/authors/{author_id}",
    summary="Gets an author by id.",
    response_model=aus.Author,
    responses={status.HTTP_404_NOT_FOUND: {"model": aus.AuthorNotFoundError}},
    tags=["authors"],
)
def get_author_endpoint(author_id: int, db: Session = Depends(get_db)):
    db_author = ah.get_author(db, author_id=author_id)
    if db_author is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"author_id": author_id, "message": "Author not found."},
        )
    return db_author


@author_router.post(
    "/authors/{author_id}/books",
    summary="Create a book for an author.",
    response_model=bs.Book,
    responses={status.HTTP_404_NOT_FOUND: {"model": aus.AuthorNotFoundError}},
    tags=["authors"],
)
def get_author_endpoint(author_id: int, book: bs.BookBase, db: Session = Depends(get_db)):
    db_author = ah.get_author(db, author_id=author_id)
    if db_author is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"author_id": author_id, "message": "Author not found."},
        )

    db_book = bh.get_book_by_name_and_author_id(db, book.title, author_id)
    # New book
    if db_book is None:
        book = bs.BookCreate(
            **{**book.dict()}, **{"author_id": db_author.author_id}
        )
        db_book = bh.create_book(db, book)

    return db_book
