from pydantic import BaseModel


class Post(BaseModel):
    id: str
    content: str
    state: str
