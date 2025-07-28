from cms_service.domain.graphs.execute_subtopic_research_graph.state.topic_research_execution_state import (
    SubtopicResearchExecutionState,
)
from cms_service.domain.prompts.baml_client.async_client import b as llm
from cms_service.domain.services.utils import get_today_str
import asyncio
from cms_service.domain.graphs.execute_subtopic_research_graph.state.topic_research_execution_state import (
    SearchResultSummary,
)


async def summarize_search_results_node(state: SubtopicResearchExecutionState) -> dict:
    research_summaries = await asyncio.gather(
        *[
            llm.SummarizeResearchResult(research_result=search_result.content, date=get_today_str())
            for search_result in state.search_results
        ]
    )

    result = []
    for search_result, research_summary in zip(state.search_results, research_summaries):
        result.append(
            SearchResultSummary(title=search_result.title, url=search_result.url, content=research_summary.summary, id=search_result.id)
        )

    return {"search_result_summaries": result}
