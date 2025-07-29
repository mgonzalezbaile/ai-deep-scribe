from pymongo import MongoClient
from cms_service.domain.models.post import Post
from cms_service.domain.services.post_repository import PostRepository
from cms_service.domain.errors import NotFoundError


class PostRepositoryMongo(PostRepository):
    def __init__(self, connection_string: str, database_name: str):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.posts_collection = self.db.posts

    async def save(self, post: Post):
        post_data = post.model_dump()
        self.posts_collection.replace_one({"id": post.id}, post_data, upsert=True)

    async def find_by_id(self, post_id: str) -> Post:
        post_data = self.posts_collection.find_one({"id": post_id})
        if post_data:
            return Post(**post_data)
        else:
            raise NotFoundError(f"Post with id {post_id} not found")
