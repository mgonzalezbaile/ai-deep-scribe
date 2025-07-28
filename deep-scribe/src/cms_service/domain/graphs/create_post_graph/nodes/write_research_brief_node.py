from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentState
from cms_service.domain.prompts.baml_client.async_client import b as llm
from cms_service.domain.services.utils import get_today_str
from langchain_core.messages import get_buffer_string


async def write_research_brief_node(state: AgentState) -> dict:
    messages = state["messages"]

    response = await llm.WriteResearchBrief(messages=get_buffer_string(messages), date=get_today_str())

    return {"research_brief": response.research_question}
