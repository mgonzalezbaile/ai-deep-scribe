from langgraph.graph import END, START, StateGraph
from cms_service.domain.graphs.orchestrate_research_graph.nodes.execute_research_node import (
    execute_research_node,
)
from cms_service.domain.graphs.orchestrate_research_graph.nodes.plan_research_node import plan_research_node
from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import (
    ResearchOrchestrationState,
)
from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import Nodes

orchestrate_research_graph_builder = StateGraph(ResearchOrchestrationState)
orchestrate_research_graph_builder.add_node(Nodes.PLAN_RESEARCH.value, plan_research_node)
orchestrate_research_graph_builder.add_node(Nodes.EXECUTE_RESEARCH.value, execute_research_node)

orchestrate_research_graph_builder.add_edge(START, Nodes.PLAN_RESEARCH.value)
orchestrate_research_graph_builder.add_edge(Nodes.PLAN_RESEARCH.value, Nodes.EXECUTE_RESEARCH.value)
orchestrate_research_graph_builder.add_edge(Nodes.EXECUTE_RESEARCH.value, END)

orchestrate_research_graph = orchestrate_research_graph_builder.compile()
