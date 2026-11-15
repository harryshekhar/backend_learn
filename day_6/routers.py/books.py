from fastapi import APIRouter, Depends

from dependenccies import get_book_service
from schemas.book import bookcreate , bookresponses
from services.book_service import bookservice

router = APIRouter()


@router.get("/books", response_model=list[bookresponses])
def get_books(service: bookservice  =  Depends(get_book_service)):


@router.post("/books", response_model=BookResponse)
def create_book(
    book: BookCreate, service: BookService = Depends(get_book_service)
):
    return service.add_book(book)