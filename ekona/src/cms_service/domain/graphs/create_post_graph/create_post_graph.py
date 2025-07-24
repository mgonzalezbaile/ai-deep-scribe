from cms_service.domain.graphs.create_post_graph.nodes.clarify_with_user_node import clarify_with_user
from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentInputState, AgentState
from langgraph.graph import StateGraph
from langgraph.graph import START, END
from langgraph.graph.state import CompiledStateGraph


async def create_post_graph() -> CompiledStateGraph:
    create_post_graph_builder = StateGraph(AgentState, input=AgentInputState)
    create_post_graph_builder.add_node("clarify_with_user", clarify_with_user)
    # deep_researcher_builder.add_node("write_research_brief", write_research_brief)
    # deep_researcher_builder.add_node("research_supervisor", supervisor_subgraph)
    # deep_researcher_builder.add_node("final_report_generation", final_report_generation)
    create_post_graph_builder.add_edge(START, "clarify_with_user")
    # deep_researcher_builder.add_edge("research_supervisor", "final_report_generation")
    # deep_researcher_builder.add_edge("final_report_generation", END)
    create_post_graph_builder.add_edge("clarify_with_user", END)

    create_post = create_post_graph_builder.compile()

    return create_post
