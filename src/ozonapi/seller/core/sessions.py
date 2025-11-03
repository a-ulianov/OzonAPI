import asyncio
from contextlib import asynccontextmanager
from typing import AsyncIterator
from aiohttp import ClientSession, ClientTimeout, TCPConnector

from ...infrastructure.logging import ozonapi_logger as logger


class SessionManager:
    """Менеджер для управления HTTP-сессиями."""

    def __init__(
            self,
            timeout: float = 30.0,
            connector_limit: int = 100,
            instance_logger = logger
    ) -> None:
        self._sessions: dict[str, ClientSession] = {}
        self._session_refs: dict[str, set[int]] = {}
        self._lock = asyncio.Lock()
        self._timeout = ClientTimeout(total=timeout)
        self._connector_limit = connector_limit
        self._logger = instance_logger

    @staticmethod
    def _get_headers(client_id: str, api_key: str, token: str) -> dict:
        """Возвращает заголовки авторизации в зависимости от типа авторизации."""
        if token:
            return {"Authorization": f"Bearer {token}"}
        elif api_key and client_id:
            return {
                "Client-Id": client_id,
                "Api-Key": api_key,
            }
        else:
            raise ValueError("Недостаточно данных для авторизации")

    @asynccontextmanager
    async def get_session(self, client_id: str, api_key: str, instance_id: int, token: str = None) -> AsyncIterator[ClientSession]:
        """
        Получает сессию для client_id.

        Args:
            client_id: Идентификатор клиента
            api_key: Ключ API
            token: OAuth-токен
            instance_id: ID экземпляра

        Yields:
            ClientSession: HTTP-сессия
        """
        async with self._lock:
            if client_id not in self._sessions:
                self._sessions[client_id] = ClientSession(
                    headers=self._get_headers(client_id, api_key, token),
                    timeout=self._timeout,
                    connector=TCPConnector(limit=self._connector_limit)
                )
                self._session_refs[client_id] = set()
                self._logger.debug(f"Создана новая сессия для ClientID {client_id}")

            self._session_refs[client_id].add(instance_id)

        try:
            yield self._sessions[client_id]
        finally:
            async with self._lock:
                if client_id in self._session_refs:
                    self._session_refs[client_id].discard(instance_id)

    async def close_session(self, client_id: str) -> None:
        """Закрывает сессию для client_id."""
        async with self._lock:
            if client_id in self._sessions:
                if client_id in self._session_refs and self._session_refs[client_id]:
                    return
                session = self._sessions.pop(client_id)
                self._session_refs.pop(client_id, None)
                if not session.closed:
                    await session.close()
                    self._logger.debug(f"Сессия для ClientID {client_id} закрыта")

    async def close_all(self) -> None:
        """Закрывает все сессии."""
        async with self._lock:
            for client_id, session in list(self._sessions.items()):
                if not session.closed:
                    await session.close()
                    self._logger.debug(f"Сессия для ClientID {client_id} закрыта")
            self._sessions.clear()
            self._session_refs.clear()
        self._logger.debug("Все сессии закрыты")
