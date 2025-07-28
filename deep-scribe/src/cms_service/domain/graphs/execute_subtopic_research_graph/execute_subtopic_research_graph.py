from langgraph.graph import END, START, StateGraph
from cms_service.domain.graphs.execute_subtopic_research_graph.state.topic_research_execution_state import (
    SubtopicResearchExecutionState,
)
from cms_service.domain.graphs.execute_subtopic_research_graph.nodes.search_subtopic_node import (
    search_subtopic_node,
)
from cms_service.domain.graphs.execute_subtopic_research_graph.nodes.compress_content_node import (
    compress_content_node,
)
from cms_service.domain.graphs.execute_subtopic_research_graph.nodes.summarize_search_results_node import (
    summarize_search_results_node,
)
from cms_service.domain.services.search_engine import SearchEngine
from cms_service.infrastructure.di import container
import functools

search_engine = container.get(SearchEngine)
execute_topic_research_graph_builder = StateGraph(SubtopicResearchExecutionState)
execute_topic_research_graph_builder.add_node("search_subtopic", functools.partial(search_subtopic_node, search_engine=search_engine))
execute_topic_research_graph_builder.add_node("summarize_search_results", summarize_search_results_node)
execute_topic_research_graph_builder.add_node("compress_content", compress_content_node)

execute_topic_research_graph_builder.add_edge(START, "search_subtopic")
execute_topic_research_graph_builder.add_edge("search_subtopic", "summarize_search_results")
execute_topic_research_graph_builder.add_edge("summarize_search_results", "compress_content")
execute_topic_research_graph_builder.add_edge("compress_content", END)

execute_subtopic_research_graph = execute_topic_research_graph_builder.compile()
