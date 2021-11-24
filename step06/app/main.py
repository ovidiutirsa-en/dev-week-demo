from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from . routers import author_router, book_router


app = FastAPI(
    title="Endava DevWeek BHD",
    version="2021.11"
)

Instrumentator().instrument(app).expose(app)


@app.get(
    "/",
    summary="Demo endpoint, used for health checks.",
    tags=["demo"],
)
async def root():
    return {"message": "Hello World from Step 06"}


app.include_router(book_router)
app.include_router(author_router)
