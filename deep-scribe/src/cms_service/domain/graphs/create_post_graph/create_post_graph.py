from cms_service.domain.graphs.create_post_graph.nodes.clarify_with_user_node import clarify_with_user_node
from cms_service.domain.graphs.create_post_graph.nodes.write_research_brief_node import write_research_brief_node
from cms_service.domain.graphs.create_post_graph.nodes.generate_post_node import generate_post_node
from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentInputState, AgentState, Nodes
from langgraph.graph import StateGraph
from langgraph.graph import START, END

from langgraph.pregel import Pregel

from cms_service.domain.graphs.orchestrate_research_graph.state.research_orchestration_state import (
    ResearchOrchestrationState,
)


def create_create_post_graph(orchestrate_research_graph: Pregel):
    def _route_after_clarifying(state: AgentState) -> str:
        """Route to the appropriate next node based on the next_step decision."""
        if state["next_step"] == Nodes.CLARIFY_WITH_USER:
            return END
        elif state["next_step"] == Nodes.WRITE_RESEARCH_BRIEF:
            return Nodes.WRITE_RESEARCH_BRIEF.value
        else:
            raise ValueError(f"Invalid next_step: {state['next_step']}")

    async def _orchestrate_research_wrapper(state: AgentState) -> dict:
        """Wrapper to transform AgentState to ResearchOrchestrationState and back."""
        # Transform AgentState to ResearchOrchestrationState
        research_state = ResearchOrchestrationState(research_brief=state["research_brief"])

        # Run the research orchestration subgraph
        result = await orchestrate_research_graph.ainvoke(research_state)

        # Transform back to AgentState format
        return {
            "raw_notes": result["research_results"],
        }

    create_post_graph_builder = StateGraph(AgentState, input=AgentInputState)
    create_post_graph_builder.add_node(Nodes.CLARIFY_WITH_USER.value, clarify_with_user_node)
    create_post_graph_builder.add_node(Nodes.WRITE_RESEARCH_BRIEF.value, write_research_brief_node)
    create_post_graph_builder.add_node(Nodes.ORCHESTRATE_RESEARCH.value, _orchestrate_research_wrapper)
    create_post_graph_builder.add_node(Nodes.GENERATE_POST.value, generate_post_node)

    create_post_graph_builder.add_edge(START, Nodes.CLARIFY_WITH_USER.value)
    create_post_graph_builder.add_conditional_edges(
        Nodes.CLARIFY_WITH_USER.value,
        _route_after_clarifying,
        {
            END: END,
            Nodes.WRITE_RESEARCH_BRIEF.value: Nodes.WRITE_RESEARCH_BRIEF.value,
        },
    )
    create_post_graph_builder.add_edge(Nodes.WRITE_RESEARCH_BRIEF.value, Nodes.ORCHESTRATE_RESEARCH.value)
    create_post_graph_builder.add_edge(Nodes.ORCHESTRATE_RESEARCH.value, Nodes.GENERATE_POST.value)
    create_post_graph_builder.add_edge(Nodes.GENERATE_POST.value, END)

    return create_post_graph_builder.compile()
