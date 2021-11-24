from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from .response_models import BookRM, BookNotFoundRM, BookListRM


app = FastAPI(
    title="Endava DevWeek BHD",
    version="2021.11"
)

books = [
    {"book_id": 1, "name": "Angel Of Earth", "author": "Constance Adkins", "page_count": 173, "price": 7.92},
    {"book_id": 2, "name": "Butcher Of The Land", "author": "Syed Lowry", "page_count": 190, "price": 6.69},
    {"book_id": 3, "name": "Priests Of The World", "author": "Clara Macleod", "page_count": 101, "price": 5.43},
    {"book_id": 4, "name": "Robots Of Utopia", "author": "Alima Crouch", "page_count": 160, "price": 9.74},
    {"book_id": 5, "name": "Men And Spies", "author": "Andreea Steadman", "page_count": 131, "price": 8.95},
    {"book_id": 6, "name": "Serpents And Heroes", "author": "Constance Adkins", "page_count": 149, "price": 3.98},
    {"book_id": 7, "name": "Love Of Tomorrow", "author": "Jon-Paul East", "page_count": 185, "price": 4.0},
    {"book_id": 8, "name": "Argument Of The End", "author": "Clara Macleod", "page_count": 153, "price": 8.5},
    {"book_id": 9, "name": "Weep For My Past", "author": "Andreea Steadman", "page_count": 188, "price": 8.93},
    {"book_id": 10, "name": "Vanish In The Mines", "author": "Constance Adkins", "page_count": 189, "price": 8.01},
]


@app.get(
    "/",
    summary="Demo endpoint, used for health checks.",
)
async def root():
    return {"message": "Hello World from Step 03"}


@app.get(
    "/books/{book_id}",
    summary="Gets a book by id.",
    response_model=BookRM,
    responses={status.HTTP_404_NOT_FOUND: {"model": BookNotFoundRM}},
)
async def get_book(book_id: int):

    for book in books:
        if book["id"] == book_id:
            return book

    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"id": book_id, "message": "Book not found."})


@app.get(
    "/books/",
    summary="Gets a list of books with pagination.",
    response_model=BookListRM,
)
async def get_books(page_id: int = 0, page_size: int = 5):

    start_item = min(page_id * page_size, len(books))
    stop_item = min((page_id + 1) * page_size, len(books))

    return {
        "total_count": len(books),
        "total_pages": len(books) // page_size,
        "page_id": page_id,
        "page_size": stop_item - start_item,
        "items_on_page": stop_item - start_item,
        "books": books[start_item:stop_item],
    }
