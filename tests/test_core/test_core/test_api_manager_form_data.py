"""Тесты режима multipart/form-data в APIManager._request."""
from unittest.mock import Mock

import aiohttp
import pytest


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

    def __init__(self, status=200, json_data=None):
        self.status = status
        self._json = json_data if json_data is not None else {}

    async def read(self):
        return b""

    async def json(self, content_type=None):
        return self._json


class _Session:
    """Заглушка aiohttp-сессии, запоминающая kwargs запроса."""

    def __init__(self, response):
        self._response = response
        self.last_kwargs = None

    def request(self, method, url, **kwargs):
        self.last_kwargs = kwargs
        return _ACM(self._response)


def _wire(api_manager, session):
    """Подменяет транспорт и ограничители для прямого вызова _request."""
    session_manager = Mock()
    session_manager.get_session = Mock(return_value=_ACM(session))
    api_manager._session_manager = session_manager

    rate_limiter = Mock()
    rate_limiter.instance_limiter = _ACM(None)
    rate_limiter.client_limiter = _ACM(None)
    api_manager._rate_limiter = rate_limiter

    api_manager._create_retry_decorator = lambda: (lambda fn: fn)


class TestFormDataRequest:
    """Тесты режима отправки multipart/form-data."""

    @pytest.mark.asyncio
    async def test_form_data_is_sent_as_data(self, api_manager):
        """При form_data тело отправляется как data, а не json."""
        session = _Session(_Response(status=200, json_data={"id": 1}))
        _wire(api_manager, session)

        form = aiohttp.FormData()
        form.add_field("name", "value")

        result = await api_manager._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/create",
            form_data=form,
        )

        assert result == {"id": 1}
        assert session.last_kwargs.get("data") is form
        assert "json" not in session.last_kwargs

    @pytest.mark.asyncio
    async def test_json_path_unchanged(self, api_manager):
        """Без form_data тело по-прежнему отправляется как json."""
        session = _Session(_Response(status=200, json_data={"ok": True}))
        _wire(api_manager, session)

        result = await api_manager._request(
            method="post",
            api_version="v1",
            endpoint="any",
            payload={"a": 1},
        )

        assert result == {"ok": True}
        assert session.last_kwargs.get("json") == {"a": 1}
        assert "data" not in session.last_kwargs
