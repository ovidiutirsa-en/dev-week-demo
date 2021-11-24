from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..response_models.book import BookRM, BookNotFoundRM, BookListRM
from ..services.book_handler import get_book, get_books_with_pagination

book_router = APIRouter()


@book_router.get(
    "/books/{book_id}",
    summary="Gets a book by id.",
    response_model=BookRM,
    responses={status.HTTP_404_NOT_FOUND: {"model": BookNotFoundRM}},
    tags=["books"],
)
async def get_book_endpoint(book_id: int):

    response_status, book = get_book(book_id)
    if response_status:
        return book

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"id": book_id, "message": "Book not found."})


@book_router.get(
    "/books/",
    summary="Gets a list of books with pagination.",
    response_model=BookListRM,
    tags=["books"],
)
async def get_books_endpoint(page_id: int = 0, page_size: int = 5):

    book_list = get_books_with_pagination(page_id, page_size)
    return book_list
