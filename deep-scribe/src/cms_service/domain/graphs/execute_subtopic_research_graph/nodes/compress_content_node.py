from cms_service.domain.graphs.execute_subtopic_research_graph.state.topic_research_execution_state import (
    SubtopicResearchExecutionState,
)
from cms_service.domain.prompts.baml_client.async_client import b as llm
from cms_service.domain.services.utils import get_today_str


async def compress_content_node(state: SubtopicResearchExecutionState) -> dict:
    content = "\n".join([result.model_dump_json() for result in state.search_result_summaries])

    compressed_content = await llm.CompressContent(content=content, date=get_today_str())

    return {"compressed_content": compressed_content}
