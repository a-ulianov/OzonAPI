"""Тесты методов SessionManager."""
import pytest
from unittest.mock import patch, AsyncMock


class TestSessionMethods:
    """Тесты методов SessionManager."""

    def test_get_active_instances_count(self, session_manager):
        """Тест получения количества активных инстансов."""
        # Нет клиента
        assert session_manager.get_active_instances_count("unknown") == 0

        # Добавляем тестовые данные
        session_manager._session_refs["test_client"] = {1, 2, 3}
        assert session_manager.get_active_instances_count("test_client") == 3

    def test_has_active_instances(self, session_manager):
        """Тест проверки наличия активных инстансов."""
        # Нет активных инстансов
        assert not session_manager.has_active_instances()

        # Добавляем активные инстансы
        session_manager._session_refs["client1"] = {1}
        session_manager._session_refs["client2"] = set()  # Пустой

        assert session_manager.has_active_instances()

    @pytest.mark.asyncio
    async def test_remove_instance_method_closes_session(self, session_manager):
        """Тест что remove_instance закрывает сессию при удалении последнего инстанса."""
        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.closed = False
            mock_session.close = AsyncMock()
            mock_session_class.return_value = mock_session

            # Создаем сессию с одним инстансом
            session_manager._sessions["client5"] = mock_session
            session_manager._session_refs["client5"] = {1}

            # Удаляем единственный инстанс
            await session_manager.remove_instance("client5", 1)

            # Сессия должна быть закрыта
            assert mock_session.close.called
            assert "client5" not in session_manager._sessions
            assert "client5" not in session_manager._session_refs

    @pytest.mark.asyncio
    async def test_remove_instance_preserves_session(self, session_manager):
        """Тест что remove_instance сохраняет сессию при наличии других инстансов."""
        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.closed = False
            mock_session.close = AsyncMock()
            mock_session_class.return_value = mock_session

            # Создаем сессию с двумя инстансами
            session_manager._sessions["client6"] = mock_session
            session_manager._session_refs["client6"] = {1, 2}

            # Удаляем только один инстанс
            await session_manager.remove_instance("client6", 1)

            # Сессия не должна быть закрыта
            assert not mock_session.close.called
            assert "client6" in session_manager._sessions
            assert session_manager._session_refs["client6"] == {2}

    @pytest.mark.asyncio
    async def test_close_session_method(self, session_manager):
        """Тест метода close_session."""
        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.closed = False
            mock_session.close = AsyncMock()
            mock_session_class.return_value = mock_session

            # Создаем сессию напрямую (без контекстного менеджера)
            session_manager._sessions["client7"] = mock_session
            session_manager._session_refs["client7"] = {1}

            # Принудительно закрываем сессию
            await session_manager.close_session("client7")

            # Сессия должна быть закрыта
            assert mock_session.close.called
            assert "client7" not in session_manager._sessions
            assert "client7" not in session_manager._session_refs

    @pytest.mark.asyncio
    async def test_close_all_method(self, session_manager):
        """Тест метода close_all."""
        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session1 = AsyncMock()
            mock_session1.closed = False
            mock_session1.close = AsyncMock()

            mock_session2 = AsyncMock()
            mock_session2.closed = False
            mock_session2.close = AsyncMock()

            # Создаем сессии напрямую (без контекстного менеджера)
            session_manager._sessions["client8"] = mock_session1
            session_manager._session_refs["client8"] = {1}

            session_manager._sessions["client9"] = mock_session2
            session_manager._session_refs["client9"] = {1}

            # Закрываем все принудительно
            await session_manager.close_all()

            # Все сессии должны быть закрыты
            assert mock_session1.close.called
            assert mock_session2.close.called
            assert session_manager._sessions == {}
            assert session_manager._session_refs == {}