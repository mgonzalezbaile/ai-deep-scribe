from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import (
    ResearchOrchestrationState,
)
from cms_service.domain.prompts.baml_client.async_client import b as llm
from cms_service.domain.services.utils import get_today_str
from cms_service.infrastructure.config import settings


async def plan_research_node(state: ResearchOrchestrationState) -> dict:
    research_plan = await llm.PlanResearch(
        user_research_question=state.research_brief,
        date=get_today_str(),
        max_subtopics=settings.MAX_SUBTOPICS,
    )

    return {"research_plan": research_plan}
