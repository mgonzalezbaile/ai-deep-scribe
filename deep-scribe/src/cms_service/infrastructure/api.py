from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from cms_service.domain.errors import DomainError
from cms_service.domain.use_cases.create_post_command import CreatePostCommand, CreatePostCommandHandler
from cms_service.infrastructure.api_middlewares import ExceptionHandlingMiddleware
from cms_service.infrastructure.di.di import bootstrap


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events for the API."""
    yield


container = bootstrap()

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
    try:
        command = CreatePostCommand(user_request=request.user_request)
        handler = container.get(CreatePostCommandHandler)

        post = await handler.execute(command)

        return JSONResponse(
            content=post.model_dump(),
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
