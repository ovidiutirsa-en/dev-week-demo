from ._mock_data import books
from typing import Dict, List, Tuple


def _get_author_books(author_id: int) -> List[Dict]:
    """
    Gets all books for an author.

    :param author_id: The author id.
    :return: List of books for author.
    """
    author_books = [book.copy() for book in books if book["author_id"] == author_id]
    return author_books


def get_author(author_id: int) -> Tuple[bool, Dict]:
    """
    Gets an author data.

    :param author_id: The author id.
    :return: The author data as a dictionary, if found.
    """
    author_books = _get_author_books(author_id)

    result = {}
    status = False

    # Author was not found
    if not author_books:
        return status, result

    # Author was found
    status = True

    result["author"] = author_books[0]["author"]
    result["author_id"] = author_books[0]["author_id"]
    for book in author_books:
        del book["author_id"]
        del book["author"]
    result["books"] = author_books
    result["book_count"] = len(books)

    return status, result


def get_authors() -> List[Dict]:
    """
    Gets a list of authors.

    :return: List of authors data as dictionaries.
    """
    unique_author_ids = set()
    authors = []
    for book in books:
        if book["author_id"] in unique_author_ids:
            continue

        unique_author_ids.add(book["author_id"])
        author = {"author_id": book["author_id"], "author": book["author"]}
        authors.append(author)

    return sorted(authors, key=lambda entry: entry["author_id"])


def get_authors_with_pagination(page_id: int = 0, page_size: int = 5):
    """
    Gets authors with pagination.

    :param page_id: The start page, 0-indexed
    :param page_size: The page size.
    :return:
    """
    authors = get_authors()
    start_item = min(page_id * page_size, len(authors))
    stop_item = min((page_id + 1) * page_size, len(authors))
    total_pages = len(authors) // page_size

    return {
        "pagination": {
            "total_count": len(authors),
            "total_pages": total_pages,
            "page_id": page_id,
            "page_size": stop_item - start_item,
            "items_on_page": stop_item - start_item,
        },
        "authors": authors[start_item:stop_item],
    }
