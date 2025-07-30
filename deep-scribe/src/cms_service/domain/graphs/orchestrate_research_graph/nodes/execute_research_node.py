from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import (
    ResearchOrchestrationState,
)
from cms_service.domain.graphs.execute_subtopic_research_graph.state.topic_research_execution_state import (
    SubtopicResearchExecutionState,
)
import asyncio
from langgraph.pregel import Pregel
from typing import Awaitable, Callable


def execute_research_node(execute_subtopic_research_graph: Pregel) -> Callable[[ResearchOrchestrationState], Awaitable[dict]]:
    async def _execute_research_node(state: ResearchOrchestrationState) -> dict:
        topic_research_tasks = []

        for subtopic in state.research_plan.subtopics:
            topic_research_tasks.append(execute_subtopic_research_graph.ainvoke(SubtopicResearchExecutionState(subtopic=subtopic)))

        research_results = await asyncio.gather(*topic_research_tasks)

        return {"research_results": research_results}

    return _execute_research_node
