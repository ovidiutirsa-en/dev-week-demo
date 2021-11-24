from pydantic import BaseModel
from typing import Optional


class ItemNotFoundRM(BaseModel):
    message: Optional[str] = "Item not found"


class PaginationRM(BaseModel):
    total_count: int
    total_pages: int
    page_id: int
    page_size: int
    items_on_page: int
