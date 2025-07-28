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

    async def execute(self, command: CreatePostCommand) -> Post:
        initial_state = AgentState(messages=[AIMessage(content=command.user_request)])
        output_state = await self.create_post_graph.ainvoke(input=initial_state)

        post = Post(content=output_state["result"])

        self.post_repository.save(post)

        return post
