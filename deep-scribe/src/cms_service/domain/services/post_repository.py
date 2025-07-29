from cms_service.domain.models.post import Post
from abc import ABC, abstractmethod


class PostRepository(ABC):
    @abstractmethod
    async def save(self, post: Post):
        raise NotImplementedError

    @abstractmethod
    async def find_by_id(self, post_id: str) -> Post:
        raise NotImplementedError
