from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from ..response_models.author import AuthorRM, AuthorNotFoundRM, AuthorListRM
from ..services.author_handler import get_author, get_authors_with_pagination

author_router = APIRouter()


@author_router.get(
    "/authors/{author_id}",
    summary="Gets an author by id.",
    response_model=AuthorRM,
    responses={status.HTTP_404_NOT_FOUND: {"model": AuthorNotFoundRM}},
    tags=["authors"],
)
async def get_author_endpoint(author_id: int):

    response_status, author = get_author(author_id)
    if response_status:
        return author

    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"author_id": author_id, "message": "Author not found."},
    )


@author_router.get(
    "/authors/",
    summary="Gets a list of books with pagination.",
    response_model=AuthorListRM,
    tags=["authors"],
)
async def get_authors_endpoint(page_id: int = 0, page_size: int = 5):

    author_list = get_authors_with_pagination(page_id, page_size)
    return author_list
