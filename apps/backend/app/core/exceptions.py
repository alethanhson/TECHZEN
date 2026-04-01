from typing import Any, Optional


class AppException(Exception):
    """Base exception for all application errors. Caught by global handler."""

    def __init__(
        self,
        message: str,
        status_code: int = 400,
        error_code: str = "APP_ERROR",
        data: Any = None,
    ):
        self.message = message
        self.status_code = status_code
        self.error_code = error_code
        self.data = data
        super().__init__(message)


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(message, 404, "NOT_FOUND")


class AlreadyExistsException(AppException):
    def __init__(self, message: str = "Resource already exists"):
        super().__init__(message, 409, "ALREADY_EXISTS")


class UnauthorizedException(AppException):
    def __init__(self, message: str = "Unauthorized"):
        super().__init__(message, 401, "UNAUTHORIZED")


class ForbiddenException(AppException):
    def __init__(self, message: str = "Forbidden"):
        super().__init__(message, 403, "FORBIDDEN")


class RateLimitException(AppException):
    def __init__(self, message: str = "Too many requests"):
        super().__init__(message, 429, "RATE_LIMIT_EXCEEDED")