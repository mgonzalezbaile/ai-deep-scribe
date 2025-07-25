from abc import abstractmethod
from typing import List, Optional
from pydantic import BaseModel


class SearchEngine:
    @abstractmethod
    async def search(self, query: str) -> List["SearchResult"]:
        pass


class SearchResult(BaseModel):
    id: Optional[int] = None
    title: str
    url: str
    content: str
    score: float
