import asyncio
from unittest.mock import AsyncMock, patch
import pytest
from aiohttp import ClientSession, ClientTimeout, TCPConnector

from src.ozonapi.seller.core.sessions import SessionManager


class TestSessionManager:
    """Тесты для SessionManager."""

    @pytest.fixture
    def session_manager(self):
        """Фикстура для создания экземпляра SessionManager."""
        return SessionManager(timeout=30.0, connector_limit=100)

    @pytest.fixture
    def mock_client_session_class(self):
        """Фикстура для мока класса ClientSession."""
        with patch('src.ozonapi.seller.core.sessions.ClientSession') as mock_session_class:
            mock_session_instance = AsyncMock(spec=ClientSession)
            mock_session_instance.closed = False
            mock_session_class.return_value = mock_session_instance
            yield mock_session_class

    @pytest.fixture
    def mock_client_session_instance(self, mock_client_session_class):
        """Фикстура для мока экземпляра ClientSession."""
        return mock_client_session_class.return_value

    @pytest.mark.asyncio
    async def test_get_session_creates_new_session(self, session_manager, mock_client_session_class,
                                                   mock_client_session_instance):
        """Тест создания новой сессии при первом обращении."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id = 123

        async with session_manager.get_session(client_id, api_key, instance_id) as session:
            assert session is mock_client_session_instance

        # Проверяем, что сессия создана с правильными параметрами
        mock_client_session_class.assert_called_once()
        call_args = mock_client_session_class.call_args
        assert call_args[1]['headers']['Client-Id'] == client_id
        assert call_args[1]['headers']['Api-Key'] == api_key
        assert isinstance(call_args[1]['timeout'], ClientTimeout)
        assert call_args[1]['timeout'].total == 30.0
        assert isinstance(call_args[1]['connector'], TCPConnector)
        assert call_args[1]['connector']._limit == 100

    @pytest.mark.asyncio
    async def test_get_session_reuses_existing_session(self, session_manager, mock_client_session_class,
                                                       mock_client_session_instance):
        """Тест повторного использования существующей сессии."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id_1 = 123
        instance_id_2 = 456

        # Первое использование
        async with session_manager.get_session(client_id, api_key, instance_id_1) as session1:
            assert session1 is mock_client_session_instance

        # Второе использование - должна быть переиспользована та же сессия
        async with session_manager.get_session(client_id, api_key, instance_id_2) as session2:
            assert session2 is mock_client_session_instance

        # ClientSession должен быть создан только один раз
        assert mock_client_session_class.call_count == 1

    @pytest.mark.asyncio
    async def test_get_session_different_clients_create_different_sessions(self, session_manager):
        """Тест создания разных сессий для разных client_id."""
        with patch('src.ozonapi.seller.core.sessions.ClientSession') as mock_session_class:
            # Создаем разные моки для разных вызовов
            mock_session_instances = [AsyncMock(spec=ClientSession) for _ in range(2)]
            for mock_instance in mock_session_instances:
                mock_instance.closed = False

            mock_session_class.side_effect = mock_session_instances

            client_id_1 = "client_1"
            client_id_2 = "client_2"
            api_key = "test_api_key"
            instance_id = 123

            async with session_manager.get_session(client_id_1, api_key, instance_id) as session1:
                pass

            async with session_manager.get_session(client_id_2, api_key, instance_id) as session2:
                pass

            # Должны быть созданы две разные сессии
            assert mock_session_class.call_count == 2
            assert session1 is mock_session_instances[0]
            assert session2 is mock_session_instances[1]

    @pytest.mark.asyncio
    async def test_get_session_tracks_instance_references(self, session_manager, mock_client_session_instance):
        """Тест отслеживания ссылок на экземпляры."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id_1 = 123
        instance_id_2 = 456

        # Первый экземпляр - внутри контекста ссылка должна быть
        async with session_manager.get_session(client_id, api_key, instance_id_1) as session:
            assert session is mock_client_session_instance
            assert instance_id_1 in session_manager._session_refs[client_id]

        # После выхода из контекста ссылка удаляется
        assert instance_id_1 not in session_manager._session_refs[client_id]

        # Второй экземпляр
        async with session_manager.get_session(client_id, api_key, instance_id_2) as session:
            assert session is mock_client_session_instance
            assert instance_id_2 in session_manager._session_refs[client_id]

        # После выхода из контекста ссылка удаляется
        assert instance_id_2 not in session_manager._session_refs[client_id]

    @pytest.mark.asyncio
    async def test_close_session(self, session_manager, mock_client_session_class, mock_client_session_instance):
        """Тест закрытия конкретной сессии."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id = 123

        # Создаем сессию
        async with session_manager.get_session(client_id, api_key, instance_id):
            pass

        # Проверяем, что сессия создана
        assert client_id in session_manager._sessions

        # Закрываем сессию
        await session_manager.close_session(client_id)

        # Проверяем, что сессия закрыта и удалена
        mock_client_session_instance.close.assert_awaited_once()
        assert client_id not in session_manager._sessions
        assert client_id not in session_manager._session_refs

    @pytest.mark.asyncio
    async def test_close_session_nonexistent_client(self, session_manager):
        """Тест закрытия несуществующей сессии."""
        # Не должно быть исключения при закрытии несуществующей сессии
        await session_manager.close_session("nonexistent_client")

    @pytest.mark.asyncio
    async def test_close_all_sessions(self, session_manager):
        """Тест закрытия всех сессий."""
        with patch('src.ozonapi.seller.core.sessions.ClientSession') as mock_session_class:
            # Создаем несколько моков для разных сессий
            mock_session_instances = [AsyncMock(spec=ClientSession) for _ in range(2)]
            for mock_instance in mock_session_instances:
                mock_instance.closed = False

            mock_session_class.side_effect = mock_session_instances

            client_id_1 = "client_1"
            client_id_2 = "client_2"
            api_key = "test_api_key"
            instance_id = 123

            # Создаем несколько сессий
            async with session_manager.get_session(client_id_1, api_key, instance_id):
                pass
            async with session_manager.get_session(client_id_2, api_key, instance_id):
                pass

            # Закрываем все сессии
            await session_manager.close_all()

            # Проверяем, что все сессии закрыты и очищены
            for mock_instance in mock_session_instances:
                mock_instance.close.assert_awaited_once()
            assert len(session_manager._sessions) == 0
            assert len(session_manager._session_refs) == 0

    @pytest.mark.asyncio
    async def test_session_context_manager_removes_reference_on_exit(self, session_manager,
                                                                     mock_client_session_instance):
        """Тест удаления ссылки на экземпляр при выходе из контекста."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id = 123

        async with session_manager.get_session(client_id, api_key, instance_id) as session:
            assert session is mock_client_session_instance
            assert instance_id in session_manager._session_refs[client_id]

        # После выхода из контекста ссылка должна быть удалена
        assert instance_id not in session_manager._session_refs[client_id]

    @pytest.mark.asyncio
    async def test_multiple_instances_same_client(self, session_manager, mock_client_session_instance):
        """Тест работы нескольких экземпляров с одним client_id."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_ids = [123, 456, 789]

        # Создаем несколько экземпляров
        for instance_id in instance_ids:
            async with session_manager.get_session(client_id, api_key, instance_id) as session:
                assert session is mock_client_session_instance
                assert instance_id in session_manager._session_refs[client_id]

        # После завершения всех контекстов ссылки должны быть очищены
        assert len(session_manager._session_refs[client_id]) == 0

    def test_initialization_parameters(self):
        """Тест инициализации с различными параметрами."""
        timeout = 15.0
        connector_limit = 50

        manager = SessionManager(timeout=timeout, connector_limit=connector_limit)

        assert manager._timeout.total == timeout
        assert manager._connector_limit == connector_limit

    @pytest.mark.asyncio
    async def test_session_headers_are_correct(self, session_manager):
        """Тест корректности заголовков сессии."""
        with patch('src.ozonapi.seller.core.sessions.ClientSession') as mock_session_class:
            mock_session_instance = AsyncMock(spec=ClientSession)
            mock_session_instance.closed = False
            mock_session_class.return_value = mock_session_instance

            client_id = "test_client"
            api_key = "test_api_key"
            instance_id = 123

            async with session_manager.get_session(client_id, api_key, instance_id):
                pass

            # Проверяем заголовки
            call_kwargs = mock_session_class.call_args[1]
            assert call_kwargs['headers']['Client-Id'] == client_id
            assert call_kwargs['headers']['Api-Key'] == api_key

    @pytest.mark.asyncio
    async def test_concurrent_session_access(self, session_manager, mock_client_session_class,
                                             mock_client_session_instance):
        """Тест конкурентного доступа к сессиям."""
        client_id = "test_client"
        api_key = "test_api_key"

        async def use_session(instance_id):
            async with session_manager.get_session(client_id, api_key, instance_id) as session:
                await asyncio.sleep(0.01)
                return session

        # Запускаем несколько конкурентных задач
        tasks = [use_session(i) for i in range(5)]
        results = await asyncio.gather(*tasks)

        # Все задачи должны получить одну и ту же сессию
        assert all(result is mock_client_session_instance for result in results)
        # Сессия должна быть создана только один раз
        assert mock_client_session_class.call_count == 1

    @pytest.mark.asyncio
    async def test_session_not_closed_when_references_exist(self, session_manager, mock_client_session_instance):
        """Тест, что сессия не закрывается, пока есть активные ссылки внутри контекста."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id = 123

        # Создаем сессию и проверяем внутри контекста
        async with session_manager.get_session(client_id, api_key, instance_id):
            # Сессия существует
            assert client_id in session_manager._sessions
            # Есть активные ссылки
            assert instance_id in session_manager._session_refs[client_id]

            # Пытаемся закрыть - не должно закрыться, т.к. есть активные ссылки
            await session_manager.close_session(client_id)

            # Сессия все еще должна существовать, т.к. мы внутри контекста
            assert client_id in session_manager._sessions
            mock_client_session_instance.close.assert_not_called()

        # После выхода из контекста сессия все еще существует, но ссылок нет
        assert client_id in session_manager._sessions
        assert len(session_manager._session_refs[client_id]) == 0

    @pytest.mark.asyncio
    async def test_close_session_only_when_no_references(self, session_manager, mock_client_session_instance):
        """Тест, что сессия закрывается только когда нет активных ссылок."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id = 123

        # Создаем сессию
        async with session_manager.get_session(client_id, api_key, instance_id):
            # Внутри контекста - сессия существует
            assert client_id in session_manager._sessions

        # После выхода из контекста - ссылок нет, но сессия еще существует
        assert client_id in session_manager._sessions
        assert len(session_manager._session_refs[client_id]) == 0

        # Теперь закрываем сессию - должна закрыться
        await session_manager.close_session(client_id)

        # Проверяем, что сессия закрыта и удалена
        mock_client_session_instance.close.assert_awaited_once()
        assert client_id not in session_manager._sessions
        assert client_id not in session_manager._session_refs

    @pytest.mark.asyncio
    async def test_multiple_references_same_session(self, session_manager, mock_client_session_class):
        """Тест работы с несколькими ссылками на одну сессию."""
        client_id = "test_client"
        api_key = "test_api_key"

        # Создаем несколько экземпляров с одним client_id
        async with session_manager.get_session(client_id, api_key, 1):
            assert 1 in session_manager._session_refs[client_id]

            async with session_manager.get_session(client_id, api_key, 2):
                assert 2 in session_manager._session_refs[client_id]
                # Обе ссылки активны
                assert len(session_manager._session_refs[client_id]) == 2

            # После выхода второго контекста - одна ссылка осталась
            assert 1 in session_manager._session_refs[client_id]
            assert 2 not in session_manager._session_refs[client_id]
            assert len(session_manager._session_refs[client_id]) == 1

        # После выхода всех контекстов - ссылок нет
        assert len(session_manager._session_refs[client_id]) == 0

        # Сессия все еще существует
        assert client_id in session_manager._sessions

        # Закрываем сессию
        await session_manager.close_session(client_id)
        assert client_id not in session_manager._sessions

    @pytest.mark.asyncio
    async def test_lock_prevents_race_conditions(self, session_manager, mock_client_session_class):
        """Тест, что блокировка предотвращает гонки условий."""
        client_id = "test_client"
        api_key = "test_api_key"

        created_sessions = []

        async def create_session(instance_id):
            async with session_manager.get_session(client_id, api_key, instance_id):
                created_sessions.append(instance_id)
                await asyncio.sleep(0.01)

        # Запускаем несколько задач одновременно
        tasks = [create_session(i) for i in range(10)]
        await asyncio.gather(*tasks)

        # Должна быть создана только одна сессия
        assert mock_client_session_class.call_count == 1
        assert len(created_sessions) == 10  # Все задачи выполнились
        assert len(session_manager._session_refs[client_id]) == 0  # Все ссылки очищены

    @pytest.mark.asyncio
    async def test_session_cleanup_after_all_references_removed(self, session_manager, mock_client_session_instance):
        """Тест очистки сессии после удаления всех ссылок."""
        client_id = "test_client"
        api_key = "test_api_key"

        # Создаем несколько ссылок
        async with session_manager.get_session(client_id, api_key, 1):
            async with session_manager.get_session(client_id, api_key, 2):
                # Обе ссылки активны
                assert len(session_manager._session_refs[client_id]) == 2

        # После выхода из всех контекстов ссылки очищены
        assert len(session_manager._session_refs[client_id]) == 0

        # Но сессия все еще существует в пуле
        assert client_id in session_manager._sessions

        # Явно закрываем сессию
        await session_manager.close_session(client_id)
        mock_client_session_instance.close.assert_awaited_once()
        assert client_id not in session_manager._sessions

    @pytest.mark.asyncio
    async def test_already_closed_session_handling(self, session_manager, mock_client_session_instance):
        """Тест обработки уже закрытой сессии."""
        client_id = "test_client"
        api_key = "test_api_key"
        instance_id = 123

        # Создаем сессию
        async with session_manager.get_session(client_id, api_key, instance_id):
            pass

        # Помечаем сессию как закрытую
        mock_client_session_instance.closed = True

        # Закрываем сессию - не должно быть попытки закрыть уже закрытую сессию
        await session_manager.close_session(client_id)

        # close() не должен вызываться для уже закрытой сессии
        mock_client_session_instance.close.assert_not_called()
        assert client_id not in session_manager._sessions

    @pytest.mark.asyncio
    async def test_session_manager_with_custom_parameters(self):
        """Тест менеджера сессий с кастомными параметрами."""
        timeout = 60.0
        connector_limit = 200

        manager = SessionManager(timeout=timeout, connector_limit=connector_limit)

        with patch('src.ozonapi.seller.core.sessions.ClientSession') as mock_session_class:
            mock_session_instance = AsyncMock(spec=ClientSession)
            mock_session_instance.closed = False
            mock_session_class.return_value = mock_session_instance

            client_id = "test_client"
            api_key = "test_api_key"
            instance_id = 123

            async with manager.get_session(client_id, api_key, instance_id):
                pass

            # Проверяем, что параметры переданы правильно
            call_args = mock_session_class.call_args[1]
            assert call_args['timeout'].total == timeout
            assert call_args['connector']._limit == connector_limit