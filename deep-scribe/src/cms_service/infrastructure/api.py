from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cms_service.domain.errors import DomainError
from cms_service.domain.graphs.create_post_graph.state.agent_state import AgentState, Nodes
from cms_service.domain.graphs.create_post_graph.create_post_graph import create_post_graph
from cms_service.infrastructure.api_middlewares import ExceptionHandlingMiddleware
from langchain_core.messages import AIMessage


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events for the API."""
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(ExceptionHandlingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CreatePostRequest(BaseModel):
    user_request: str


@app.post("/api/posts")
async def create_post(request: CreatePostRequest):
    graph = create_post_graph

    initial_state = AgentState(messages=[AIMessage(content=request.user_request)])

    try:
        output_state = await graph.ainvoke(input=initial_state)

        return JSONResponse(
            content=output_state["result"],
            status_code=201,
        )

    except DomainError as e:
        return JSONResponse(
            content={"error": str(e)},
            status_code=409,
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
