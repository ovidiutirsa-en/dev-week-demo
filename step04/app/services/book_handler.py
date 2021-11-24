from . _mock_data import books
from typing import Dict, List, Tuple


def get_book(book_id) -> Tuple[bool, Dict]:
    """
    Gets a book data.

    :param book_id: The book id.
    :return: The book data as a dictionary, if found.
    """

    for book in books:
        if book_id == book["book_id"]:
            new_book = book.copy()
            del new_book["author_id"]

            return True, book

    return False, {}


def get_books() -> List[Dict]:
    """
    Gets a list of books.

    :return: List of books data as dictionaries.
    """
    new_books = []
    for book in books:
        new_book = book.copy()
        del new_book["author_id"]
        new_books.append(new_book)

    return new_books


def get_books_with_pagination(page_id: int = 0, page_size: int = 5):
    """
    Gets books with pagination.

    :param page_id: The start page, 0-indexed
    :param page_size: The page size.
    :return:
    """
    books_ = get_books()
    start_item = min(page_id * page_size, len(books_))
    stop_item = min((page_id + 1) * page_size, len(books_))
    total_pages = len(books_) // page_size

    return {
        "pagination": {
            "total_count": len(books_),
            "total_pages": total_pages,
            "page_id": page_id,
            "page_size": stop_item - start_item,
            "items_on_page": stop_item - start_item,
        },
        "books": books_[start_item:stop_item],
    }
