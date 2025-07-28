import traceback

from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class ExceptionHandlingMiddleware(BaseHTTPMiddleware):
    """
    Middleware that catches any unhandled exceptions and converts them to 500 responses.

    This middleware should be added early in the middleware pipeline to ensure it catches
    exceptions from all other middlewares and route handlers.
    """

    async def dispatch(self, request: Request, call_next):
        try:
            return await call_next(request)
        except Exception as e:
            print(f"Unhandled exception in {request.method} {request.url.path}:")
            traceback.print_exc()

            return JSONResponse(status_code=500, content={"detail": "Internal server error"})
