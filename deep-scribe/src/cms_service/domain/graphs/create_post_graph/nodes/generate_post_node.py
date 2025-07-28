from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentState
from cms_service.domain.prompts.baml_client.async_client import b as llm
import json


async def generate_post_node(state: AgentState) -> dict:
    findings = []
    for note in state["raw_notes"]:
        finding = {}
        finding["subtopic"] = note["subtopic"].topic
        finding["findings"] = [f.model_dump() for f in note["compressed_content"].findings]
        findings.append(finding)

    response = await llm.GeneratePost(research_brief=state["research_brief"], findings=json.dumps(findings))

    return {"post": response.content}
