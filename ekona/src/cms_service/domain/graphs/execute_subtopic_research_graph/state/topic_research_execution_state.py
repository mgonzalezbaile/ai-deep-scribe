from typing import List, Optional
from cms_service.domain.prompts.baml_client.types import SubTopic
from pydantic import BaseModel
from cms_service.domain.services.search_engine import SearchResult
from cms_service.domain.prompts.baml_client.types import CompressedContent


class SubtopicResearchExecutionState(BaseModel):
    # Input
    subtopic: SubTopic

    # State progression: - populated during workflow
    search_results: List[SearchResult] = []
    search_result_summaries: List["SearchResultSummary"] = []

    # Output
    compressed_content: Optional[CompressedContent] = None


class SearchResultSummary(BaseModel):
    id: Optional[int] = None
    title: str
    url: str
    content: str
