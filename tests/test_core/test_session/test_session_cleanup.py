"""Тесты очистки сессий."""
import pytest


class TestSessionCleanup:
    """Тесты очистки сессий."""

    @pytest.mark.asyncio
    async def test_session_auto_close_on_last_instance(self, session_manager, mock_client_data):
        """Тест автоматического закрытия сессии при удалении последнего инстанса."""
        client_data = mock_client_data("client3", "key3")

        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session:
            # Сессия создана и активна
            assert not session.closed
            assert client_data["client_id"] in session_manager._sessions
            assert 1 in session_manager._session_refs[client_data["client_id"]]

        # После выхода из контекста сессия должна быть закрыта автоматически
        assert session.closed
        assert client_data["client_id"] not in session_manager._sessions
        assert client_data["client_id"] not in session_manager._session_refs

    @pytest.mark.asyncio
    async def test_session_preserved_with_multiple_instances(self, session_manager, mock_client_data):
        """Тест сохранения сессии при наличии нескольких инстансов."""
        client_data = mock_client_data("client4", "key4")

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
                assert session_manager._session_refs[client_data["client_id"]] == {1, 2}

            # После выхода из второго контекста, но пока первый активен
            assert not session.closed
            assert client_data["client_id"] in session_manager._sessions
            assert session_manager._session_refs[client_data["client_id"]] == {1}

    @pytest.mark.asyncio
    async def test_session_close_after_all_instances_exit(self, session_manager, mock_client_data):
        """Тест закрытия сессии после выхода всех инстансов."""
        client_data = mock_client_data("client5", "key5")

        async with session_manager.get_session(
            client_id=client_data["client_id"],
            api_key=client_data["api_key"],
            instance_id=1
        ) as session1:
            async with session_manager.get_session(
                client_id=client_data["client_id"],
                api_key=client_data["api_key"],
                instance_id=2
            ) as session2:
                # Оба инстанса активны
                assert not session1.closed
                assert not session2.closed
                assert session1 is session2  # Та же сессия
                assert client_data["client_id"] in session_manager._sessions

        # После выхода всех инстансов сессия должна быть закрыта
        assert session1.closed
        assert client_data["client_id"] not in session_manager._sessions
        assert client_data["client_id"] not in session_manager._session_refs

    @pytest.mark.asyncio
    async def test_session_independent_per_client(self, session_manager, mock_client_data):
        """Тест независимого управления сессиями для разных клиентов."""
        client1_data = mock_client_data("client6", "key6")
        client2_data = mock_client_data("client7", "key7")

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
                # Обе сессии активны
                assert not session1.closed
                assert not session2.closed
                assert client1_data["client_id"] in session_manager._sessions
                assert client2_data["client_id"] in session_manager._sessions

        # После выхода обе сессии должны быть закрыты
        assert session1.closed
        assert session2.closed
        assert client1_data["client_id"] not in session_manager._sessions
        assert client2_data["client_id"] not in session_manager._sessions