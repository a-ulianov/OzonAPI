"""Тесты бинарного режима ответа в APIManager._request."""
from unittest.mock import Mock

import pytest

from src.ozonapi.seller.core.exceptions import APINotFoundError


class _ACM:
    """Простой асинхронный контекст-менеджер, отдающий заданное значение."""

    def __init__(self, value):
        self.value = value

    async def __aenter__(self):
        return self.value

    async def __aexit__(self, *args):
        return False


class _Response:
    """Заглушка aiohttp-ответа."""

    def __init__(self, status, content=b"", json_data=None):
        self.status = status
        self._content = content
        self._json = json_data if json_data is not None else {}

    async def read(self):
        return self._content

    async def json(self, content_type=None):
        return self._json


class _Session:
    """Заглушка aiohttp-сессии."""

    def __init__(self, response):
        self._response = response

    def request(self, method, url, json=None, params=None):
        return _ACM(self._response)


def _wire(api_manager, response):
    """Подменяет транспорт и ограничители для прямого вызова _request."""
    session_manager = Mock()
    session_manager.get_session = Mock(return_value=_ACM(_Session(response)))
    api_manager._session_manager = session_manager

    rate_limiter = Mock()
    rate_limiter.instance_limiter = _ACM(None)
    rate_limiter.client_limiter = _ACM(None)
    api_manager._rate_limiter = rate_limiter

    api_manager._create_retry_decorator = lambda: (lambda fn: fn)


class TestBinaryRequest:
    """Тесты режима response_format='binary'."""

    @pytest.mark.asyncio
    async def test_binary_success_returns_bytes(self, api_manager):
        """Бинарный ответ возвращается как {'content': <bytes>}."""
        _wire(api_manager, _Response(status=200, content=b"%PDF-1.4 data"))

        result = await api_manager._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-pdf",
            payload={"id": 12345},
            response_format="binary",
        )

        assert result == {"content": b"%PDF-1.4 data"}

    @pytest.mark.asyncio
    async def test_binary_error_parsed_as_json(self, api_manager):
        """Ошибка бинарного эндпоинта разбирается из JSON и поднимается как исключение."""
        _wire(api_manager, _Response(status=404, json_data={"code": 5, "message": "CARRIAGE_NOT_FOUND"}))

        with pytest.raises(APINotFoundError):
            await api_manager._request(
                method="post",
                api_version="v2",
                endpoint="posting/fbs/act/get-pdf",
                payload={"id": 1},
                response_format="binary",
            )
