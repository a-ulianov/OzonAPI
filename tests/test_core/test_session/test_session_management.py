"""Тесты управления сессиями."""
import pytest


class TestSessionManagement:
    """Тесты управления сессиями."""

    @pytest.mark.asyncio
    async def test_get_session_creation(self, session_manager, mock_client_data):
        """Тест создания новой сессии."""
        client_data = mock_client_data("client1", "key1")

        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session:
            # Проверяем что создана новая сессия
            assert client_data["client_id"] in session_manager._sessions
            assert session is session_manager._sessions[client_data["client_id"]]
            assert 1 in session_manager._session_refs[client_data["client_id"]]
            assert not session.closed

    @pytest.mark.asyncio
    async def test_get_session_reuse_within_same_context(self, session_manager, mock_client_data):
        """Тест повторного использования существующей сессии в рамках одного контекста."""
        client_data = mock_client_data("client2", "key2")

        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session1:
            # Второе использование того же клиента в том же контексте
            async with session_manager.get_session(
                client_id=client_data["client_id"],
                api_key=client_data["api_key"],
                instance_id=2
            ) as session2:
                # Должна использоваться та же сессия
                assert session2 is session1
                assert session_manager._sessions[client_data["client_id"]] is session1
                # Оба инстанса должны быть зарегистрированы
                assert session_manager._session_refs[client_data["client_id"]] == {1, 2}

    @pytest.mark.asyncio
    async def test_get_session_multiple_instances_same_client(self, session_manager, mock_client_data):
        """Тест нескольких инстансов одного клиента."""
        client_data = mock_client_data("client3", "key3")

        # Первый инстанс
        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session1:
            # Второй инстанс того же клиента (вложенный контекст)
            async with session_manager.get_session(
                client_id=client_data["client_id"],
                api_key=client_data["api_key"],
                instance_id=2
            ) as session2:
                # Оба инстанса должны быть зарегистрированы
                assert session_manager._session_refs[client_data["client_id"]] == {1, 2}
                # Сессия должна быть одна и та же
                assert session1 is session2
                assert len(session_manager._sessions) == 1

    @pytest.mark.asyncio
    async def test_get_session_different_clients(self, session_manager, mock_client_data):
        """Тест сессий для разных клиентов."""
        client1_data = mock_client_data("client4", "key4")
        client2_data = mock_client_data("client5", "key5")

        async with session_manager.get_session(
            client_id=client1_data["client_id"],
            api_key=client1_data["api_key"],
            instance_id=1
        ) as session1:
            async with session_manager.get_session(
                client_id=client2_data["client_id"],
                api_key=client2_data["api_key"],
                instance_id=1
            ) as session2:
                # Должны быть две разные сессии
                assert session1 is not session2
                assert session_manager._sessions[client1_data["client_id"]] is session1
                assert session_manager._sessions[client2_data["client_id"]] is session2
                assert len(session_manager._sessions) == 2

    @pytest.mark.asyncio
    async def test_session_auto_close_on_last_instance(self, session_manager, mock_client_data):
        """Тест автоматического закрытия сессии при удалении последнего инстанса."""
        client_data = mock_client_data("client6", "key6")

        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session:
            # Сессия создана
            assert not session.closed
            assert client_data["client_id"] in session_manager._sessions

        # После выхода из контекста сессия должна быть закрыта
        assert session.closed
        assert client_data["client_id"] not in session_manager._sessions

    @pytest.mark.asyncio
    async def test_session_preserved_with_multiple_instances(self, session_manager, mock_client_data):
        """Тест сохранения сессии при наличии нескольких инстансов."""
        client_data = mock_client_data("client7", "key7")

        # Первый инстанс
        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session:
            # Второй инстанс
            async with session_manager.get_session(
                client_id=client_data["client_id"],
                api_key=client_data["api_key"],
                instance_id=2
            ):
                # Сессия не должна быть закрыта пока есть активные инстансы
                assert not session.closed
                assert client_data["client_id"] in session_manager._sessions

            # После выхода из второго контекста, но пока первый активен
            assert not session.closed
            assert client_data["client_id"] in session_manager._sessions