from cms_service.domain.graphs.execute_subtopic_research_graph.state.topic_research_execution_state import (
    SubtopicResearchExecutionState,
)
from cms_service.domain.services.search_engine import SearchEngine
from cms_service.infrastructure.config import settings


async def search_subtopic_node(state: SubtopicResearchExecutionState, search_engine: SearchEngine) -> dict:
    search_results = await search_engine.search(state.subtopic.topic, max_results=settings.MAX_SEARCH_RESULTS)
    id = 1
    for search_result in search_results:
        search_result.id = id
        id += 1

    return {"search_results": search_results}
