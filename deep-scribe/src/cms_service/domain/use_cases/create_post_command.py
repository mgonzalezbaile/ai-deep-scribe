import asyncio
import uuid
from langchain_core.messages import AIMessage

from langchain_core.messages import AIMessage
from langgraph.pregel import Pregel

from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentState
from cms_service.domain.models.post import Post
from cms_service.domain.services.post_repository import PostRepository


class CreatePostCommand:
    def __init__(self, user_request: str):
        self.user_request = user_request


class CreatePostCommandHandler:
    def __init__(self, post_repository: PostRepository, create_post_graph: Pregel):
        self.post_repository = post_repository
        self.create_post_graph = create_post_graph

    async def _generate_and_update_post_content(self, post_id: str, user_request: str):
        initial_state = AgentState(messages=[AIMessage(content=user_request)])
        output_state = await self.create_post_graph.ainvoke(input=initial_state)

        post = Post(id=post_id, content=output_state["result"], state="completed")

        await self.post_repository.save(post)

    async def execute(self, command: CreatePostCommand) -> Post:
        post = Post(id=str(uuid.uuid4()), content="", state="processing")
        await self.post_repository.save(post)

        asyncio.create_task(self._generate_and_update_post_content(post.id, command.user_request))

        return post
