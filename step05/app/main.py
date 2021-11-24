from fastapi import FastAPI
from . routers import author_router, book_router


app = FastAPI(
    title="Endava DevWeek BHD",
    version="2021.11"
)


@app.get(
    "/",
    summary="Demo endpoint, used for health checks.",
    tags=["demo"],
)
async def root():
    return {"message": "Hello World from Step 05"}


app.include_router(book_router)
app.include_router(author_router)
