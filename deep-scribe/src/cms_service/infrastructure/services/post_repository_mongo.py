from pymongo import MongoClient
from cms_service.domain.models.post import Post
from cms_service.domain.services.post_repository import PostRepository


class PostRepositoryMongo(PostRepository):
    def __init__(self, connection_string: str, database_name: str):
        self.client = MongoClient(connection_string)
        self.db = self.client[database_name]
        self.posts_collection = self.db.posts

    def save(self, post: Post):
        post_data = post.model_dump()
        self.posts_collection.insert_one(post_data)
