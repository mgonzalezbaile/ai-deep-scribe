from langgraph.graph import StateGraph, START, END
from langgraph.pregel import Pregel
import functools

from cms_service.domain.graphs.orchestrate_research_graph.nodes.execute_research_node import (
    execute_research_node,
)
from cms_service.domain.graphs.orchestrate_research_graph.nodes.plan_research_node import (
    plan_research_node,
)
from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import (
    ResearchOrchestrationState,
)
from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import Nodes


def create_orchestrate_research_graph(execute_subtopic_research_graph: Pregel):
    orchestrate_research_graph_builder = StateGraph(ResearchOrchestrationState)
    orchestrate_research_graph_builder.add_node(Nodes.PLAN_RESEARCH.value, plan_research_node)
    orchestrate_research_graph_builder.add_node(
        Nodes.EXECUTE_RESEARCH.value,
        functools.partial(execute_research_node, execute_subtopic_research_graph=execute_subtopic_research_graph),
    )

    orchestrate_research_graph_builder.add_edge(START, Nodes.PLAN_RESEARCH.value)
    orchestrate_research_graph_builder.add_edge(Nodes.PLAN_RESEARCH.value, Nodes.EXECUTE_RESEARCH.value)
    orchestrate_research_graph_builder.add_edge(Nodes.EXECUTE_RESEARCH.value, END)

    return orchestrate_research_graph_builder.compile()
