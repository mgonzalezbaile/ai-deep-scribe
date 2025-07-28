from langgraph.pregel import Pregel

from cms_service.domain.graphs.create_post_graph.create_post_graph import create_create_post_graph
from cms_service.domain.graphs.execute_subtopic_research_graph.execute_subtopic_research_graph import create_execute_subtopic_research_graph
from cms_service.domain.graphs.orchestrate_research_graph.orchestrate_research_graph import create_orchestrate_research_graph
from cms_service.domain.services.post_repository import PostRepository
from cms_service.domain.use_cases.create_post_command import CreatePostCommandHandler
from cms_service.infrastructure.services.post_repository_mongo import PostRepositoryMongo
from cms_service.infrastructure.services.search_engine_tavily import SearchEngineTavily
from cms_service.infrastructure.config import settings
from cms_service.domain.services.search_engine import SearchEngine
from common.container.container import IContainer


def register_services(container: IContainer):
    container.register(SearchEngine, factory=lambda: SearchEngineTavily(api_key=settings.TAVILY_API_KEY))
    container.register(
        PostRepository,
        factory=lambda: PostRepositoryMongo(
            connection_string=settings.MONGO_CONNECTION_STRING,
            database_name=settings.MONGO_DATABASE_NAME,
        ),
    )

    container.register(
        "execute_subtopic_research_graph",
        factory=lambda: create_execute_subtopic_research_graph(search_engine=container.get(SearchEngine)),
    )

    container.register(
        "orchestrate_research_graph",
        factory=lambda: create_orchestrate_research_graph(execute_subtopic_research_graph=container.get("execute_subtopic_research_graph")),
    )

    container.register(
        "create_post_graph",
        factory=lambda: create_create_post_graph(orchestrate_research_graph=container.get("orchestrate_research_graph")),
    )

    container.register(
        CreatePostCommandHandler,
        factory=lambda: CreatePostCommandHandler(
            post_repository=container.get(PostRepository),
            create_post_graph=container.get("create_post_graph"),
        ),
    )
