from langchain_core.messages import AIMessage, get_buffer_string
from langchain_core.runnables import RunnableConfig
from langgraph.graph import END
from langgraph.types import Command
from cms_service.domain.prompts.baml_client.async_client import b as llm
from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentState
from cms_service.domain.services.utils import get_today_str


async def clarify_with_user(state: AgentState, config: RunnableConfig):  # -> Command[Literal["write_research_brief", "__end__"]]:
    messages = state["messages"]

    response = await llm.AskForClarification(messages=get_buffer_string(messages), date=get_today_str())

    if response.need_clarification:
        return Command(goto=END, update={"messages": [AIMessage(content=response.question)]})
    # else:
    #     return Command(goto="write_research_brief", update={"messages": [AIMessage(content=response.verification)]})
