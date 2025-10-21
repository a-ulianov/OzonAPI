class APIError(Exception):
    """Базовое исключение для ошибок API."""
    def __init__(self, code: int, message: str, details: list | None = None):
        self.code = code
        self.message = message
        self.details = details or []
        super().__init__(f"API Error {code}: {message}")


class APIClientError(APIError):
    """Ошибка 400: Неверный параметр."""
    pass


class APIForbiddenError(APIError):
    """Ошибка 403: Доступ запрещён."""
    pass


class APINotFoundError(APIError):
    """Ошибка 404: Ответ не найден."""
    pass


class APIConflictError(APIError):
    """Ошибка 409: Конфликт запроса."""
    pass

class APITooManyRequestsError(APIError):
    """Ошибка 429: Слишком много запросов."""
    pass


class APIServerError(APIError):
    """Ошибка 500: Внутренняя ошибка сервера."""
    pass
