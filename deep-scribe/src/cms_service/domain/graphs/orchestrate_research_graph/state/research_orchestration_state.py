from typing import List, Optional
from enum import Enum
import operator

from cms_service.domain.prompts.baml_client.types import CompressedContent, ResearchPlan
from pydantic import BaseModel
from cms_service.domain.services.search_engine import SearchResult
from cms_service.domain.prompts.baml_client.types import ResearchSummary


def override_reducer(current_value, new_value):
    if isinstance(new_value, dict) and new_value.get("type") == "override":
        return new_value.get("value", new_value)
    else:
        return operator.add(current_value, new_value)


class Nodes(Enum):
    PLAN_RESEARCH = "plan_research"
    EXECUTE_RESEARCH = "execute_research"


class ResearchOrchestrationState(BaseModel):
    # Input
    research_brief: str

    # State progression: - populated during workflow
    research_plan: Optional[ResearchPlan] = None

    # Output
    research_results: List[CompressedContent] = []
