import pandas as pd
import requests

from typing import Dict, List, Optional


class DevWeekAPIClient:
    BASE_URL = "http://127.0.0.1:8000"
    BOOKS_PREFIX = "books"
    AUTHORS_PREFIX = "authors"

    def __init__(self, url: Optional[str] = None):
        self._base_url = url or DevWeekAPIClient.BASE_URL

    def get_authors(
            self, page_id: Optional[int] = 0, page_size: Optional[int] = 1024,
    ) -> pd.DataFrame:
        """
        Gets authors as a data frame.

        :param page_id: The id of the page.
        :param page_size: The size of the page.

        :return: Authors data frame.
        """
        # TODO handle proper pagination on client side

        url = f"{self._base_url}/{self.AUTHORS_PREFIX}"
        result = requests.get(url, params={"page_id": page_id, "page_size": page_size})

        # Raise if incorrect response code
        result.raise_for_status()

        data = result.json()["authors"]
        data_df = pd.DataFrame.from_records(data)[["author_id", "author_name"]]

        return data_df

    def get_books(
            self, page_id: Optional[int] = 0, page_size: Optional[int] = 1024,
    ) -> pd.DataFrame:
        """
        Gets books as a data frame.

        :param page_id: The id of the page.
        :param page_size: The size of the page.

        :return: Books data frame.
        """
        # TODO handle proper pagination on client side

        url = f"{self._base_url}/{self.BOOKS_PREFIX}"
        result = requests.get(url, params={"page_id": page_id, "page_size": page_size})

        # Raise if incorrect response code
        result.raise_for_status()

        data = result.json()["books"]

        if not data:
            return pd.DataFrame()

        book_df = pd.DataFrame.from_records(data)
        author_df = self.get_authors()
        data_df = pd.merge(book_df, author_df, on="author_id", how="left")

        return data_df[["book_id", "author_id", "author_name", "title", "page_count", "price"]]

    def create_author(self, author_name: str) -> Dict:
        """
        Creates an author.

        :param author_name: The author name.
        """
        url = f"{self._base_url}/{self.AUTHORS_PREFIX}"
        result = requests.post(url, json={"author_name": author_name})

        result.raise_for_status()

        return result.json()

    def create_book_for_author(self, title: str, page_count: int, price: float, author_id: int):
        """
        Creates a book for a given author id.

        :param title: Book title.
        :param page_count: Book page count.
        :param price: Book price.
        :param author_id: Author id.
        """
        # TODO create pydantic models

        url = f"{self._base_url}/{self.AUTHORS_PREFIX}/{author_id}/{self.BOOKS_PREFIX}"
        result = requests.post(url, json={"title": title, "page_count": page_count, "price": price})

        result.raise_for_status()

        return result.json()

    def provision_database(self, books_and_authors: List[Dict]):
        """
        Creates the seed data for the database using the API and API client.

        :param books_and_authors: List of dictionaries. No ids are provided.
        """
        unique_author_names = set([entry["author_name"] for entry in books_and_authors])
        authors = {}
        for author_name in unique_author_names:
            author = self.create_author(author_name)
            authors[author_name] = author

        for entry in books_and_authors:
            author_name = entry["author_name"]
            del entry["author_name"]
            entry["author_id"] = authors[author_name]["author_id"]
            self.create_book_for_author(**entry)
