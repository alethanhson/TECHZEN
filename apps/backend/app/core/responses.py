from fastapi import FastAPI, Request, Response
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError, HTTPException
from app.core.exceptions import AppException
from typing import Callable, Any
import json


def wrap_success_response(body: Any) -> dict:
    return {
        "success": True,
        "data": body,
        "message": "Successfully",
        "error": None,
    }


class UnifiedAPIRoute(APIRoute):
    """Auto-wraps successful responses in standard format."""

    def get_route_handler(self) -> Callable:
        original_handler = super().get_route_handler()

        async def handler(request: Request) -> Response:
            response: Response = await original_handler(request)

            if not hasattr(response, "body"):
                return response
            if not (200 <= response.status_code < 300):
                return response

            try:
                parsed_body = json.loads(response.body.decode("utf-8"))
            except Exception:
                return response

            # Skip if already wrapped
            if isinstance(parsed_body, dict) and {"success", "data"} <= parsed_body.keys():
                return response

            wrapped = wrap_success_response(parsed_body)
            return JSONResponse(content=wrapped, status_code=response.status_code)

        return handler


def setup_exception_handlers(app: FastAPI):
    def error_response(status_code: int, message: str, error: Any) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={
                "success": False,
                "data": None,
                "message": message,
                "error": error,
            },
        )

    @app.exception_handler(AppException)
    async def app_exception_handler(request: Request, exc: AppException):
        return error_response(
            status_code=exc.status_code,
            message=exc.message,
            error={"error_code": exc.error_code, "data": exc.data},
        )

    @app.exception_handler(HTTPException)
    async def http_exception_handler(request: Request, exc: HTTPException):
        return error_response(
            status_code=exc.status_code,
            message=exc.detail,
            error={"status_code": exc.status_code, "detail": exc.detail},
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return error_response(
            status_code=422,
            message="Validation Error",
            error=exc.errors(),
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        return error_response(
            status_code=500,
            message="Internal Server Error",
            error=str(exc),
        )