from datetime import date
from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

# BOOK MODEL

class Book(SQLModel, table = True):

    id: Optional[int] = Field(default=None, primary_key=True)

    title: str = Field(index=True)
    author: str = Field(index=True)
    pages: Optional[int] = Field(default=None)
    cover_url: Optional[str] = None

    genre: Optional[str] = None
    is_fiction: Optional[bool] = True

    reading_events = List["ReadingEvent"] = Relationship(back_populates="book")