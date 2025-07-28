from cms_service.domain.models.post import Post
from abc import ABC, abstractmethod


class PostRepository(ABC):
    @abstractmethod
    def save(self, post: Post):
        raise NotImplementedError
