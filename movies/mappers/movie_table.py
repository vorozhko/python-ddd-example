from sqlmodel import SQLModel, Field
from sqlalchemy import Column
from sqlalchemy.types import JSON
from typing import List, Optional
from uuid import uuid4


class MovieTable(SQLModel, table=True):  # This is the database table
    id: str = Field(default_factory=lambda: str(uuid4()), primary_key=True)
    title: str
    genres: List[str] = Field(default_factory=list, sa_column=Column(JSON))  # Use Column(JSON)
    ratings: List[dict] = Field(default_factory=list, sa_column=Column(JSON))  # Use Column(JSON)
    duration: int = 0
    release_date: Optional[str] = None