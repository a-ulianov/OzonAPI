"""Тесты классовых методов APIManager."""
import pytest
from unittest.mock import patch, AsyncMock

from src.ozonapi.seller.core import APIManager


class TestAPIManagerClassMethods:
    """Тесты классовых методов APIManager."""

    @pytest.mark.asyncio
    async def test_initialize_sets_initialized_flag(self, mock_method_rate_limiter_manager):
        """Тест установки флага инициализации."""
        with patch('src.ozonapi.seller.core.core.APIManager._method_rate_limiter_manager',
                   mock_method_rate_limiter_manager):
            await APIManager.initialize()

            mock_method_rate_limiter_manager.start.assert_called_once()
            assert APIManager._initialized

    @pytest.mark.asyncio
    async def test_shutdown_cleans_up_resources(self, mock_method_rate_limiter_manager, mock_session_manager):
        """Тест очистки ресурсов при завершении."""
        APIManager._initialized = True

        with patch('src.ozonapi.seller.core.core.APIManager._method_rate_limiter_manager',
                   mock_method_rate_limiter_manager), \
                patch('src.ozonapi.seller.core.core.APIManager._session_manager',
                      mock_session_manager):
            await APIManager.shutdown()

            mock_method_rate_limiter_manager.shutdown.assert_called_once()
            mock_session_manager.close_all.assert_called_once()
            assert not APIManager._initialized