from enum import Enum
from typing import Optional
from langgraph.graph import MessagesState
from langchain_core.messages import MessageLikeRepresentation
from pydantic import BaseModel, Field


class Nodes(Enum):
    CLARIFY_WITH_USER = "clarify_with_user"
    WRITE_RESEARCH_BRIEF = "write_research_brief"
    ORCHESTRATE_RESEARCH = "orchestrate_research"
    GENERATE_POST = "generate_post"


class AgentInputState(MessagesState):
    """InputState is only 'messages'"""


class AgentState(MessagesState):
    next_step: Nodes
    supervisor_messages: list[MessageLikeRepresentation]
    research_brief: Optional[str]
    raw_notes: list[str] = []
    final_report: str
    post: Optional[str]


class ClarifyWithUser(BaseModel):
    need_clarification: bool = Field(
        description="Whether the user needs to be asked a clarifying question.",
    )
    question: str = Field(
        description="A question to ask the user to clarify the report scope",
    )
    verification: str = Field(
        description="Verify message that we will start research after the user has provided the necessary information.",
    )
