from fastapi import APIRouter, status, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from .utils import get_pagination_parameters
from ..dependencies import get_db
from ..schema import book as bs
from ..services import book_handler as bh


book_router = APIRouter()


@book_router.get(
    "/books/",
    summary="Gets a list of authors.",
    response_model=bs.Books,
    tags=["books"],
)
async def get_books_endpoint(page_id: int = 0, page_size: int = 5, db: Session = Depends(get_db)):
    books = bh.get_books(db, page_id, page_size)
    books_count = bh.get_books_count(db)

    return {
        "books": books,
        "pagination": get_pagination_parameters(page_id, page_size, len(books), books_count)
    }


@book_router.get(
    "/books/{book_id}",
    summary="Gets a book by id.",
    response_model=bs.Book,
    responses={status.HTTP_404_NOT_FOUND: {"model": bs.BookNotFoundError}},
    tags=["books"],
)
def get_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    db_book = bh.get_book(db, book_id)
    if db_book is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"book_id": book_id, "message": "Book not found."},
        )
    return db_book
