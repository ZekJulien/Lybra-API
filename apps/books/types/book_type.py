from typing import TypedDict, List, Optional
from uuid import UUID

class BookPayload(TypedDict):
    isbn: str
    title: str
    summary: str
    language: str
    publication_date: str 
    cover_url: Optional[str]
    pages: int
    collection: UUID
    authors: Optional[List[UUID]]
    genres: Optional[List[UUID]]
    publishers: Optional[List[UUID]]
    themes: Optional[List[UUID]]
