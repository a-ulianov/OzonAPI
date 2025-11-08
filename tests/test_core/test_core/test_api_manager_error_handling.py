"""Тесты обработки ошибок APIManager."""
from unittest.mock import Mock

from src.ozonapi.seller.core.core import APIManager
from src.ozonapi.seller.core.exceptions import (
    APIClientError, APIForbiddenError, APIServerError
)


class TestAPIManagerErrorHandling:
    """Тесты обработки ошибок APIManager."""

    def test_error_handling_for_client_errors(self):
        """Тест обработки ошибок клиента."""
        mock_response = Mock()
        mock_response.status = 400

        data = {"code": 400, "message": "Bad request"}

        error = APIManager._handle_error_response(mock_response, data, {})

        assert isinstance(error, APIClientError)
        assert error.code == 400

    def test_error_handling_for_server_errors(self):
        """Тест обработки ошибок сервера."""
        mock_response = Mock()
        mock_response.status = 500

        data = {"code": 500, "message": "Server error"}

        error = APIManager._handle_error_response(mock_response, data, {})

        assert isinstance(error, APIServerError)
        assert error.code == 500