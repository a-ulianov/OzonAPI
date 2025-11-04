"""
Асинхронная библиотека для работы с Seller API маркетплейса Ozon с поддержкой лимитов и отложенным автоповтором запросов.

References:
    ⭐️ Поддержите проект: https://github.com/a-ulianov/OzonAPI

    💬 Обсуждение в Telegram: https://t.me/ozonapi_async

Notes:
    - Асинхронный дизайн для высокопроизводительных операций
    - Автоматическое соблюдение лимитов Ozon Seller API
    - Кеширование ответов для методов, возвращающих статичные данные
    - Экспоненциальные повторные попытки запросов при сбоях
    - Гибкая конфигурация через классы, переменные окружения или .env
    - Одновременная работа с несколькими кабинетами
    - Поддержка OAuth-авторизации
    - Все методы содержат подробные docstrings с примерами


Examples:
    import asyncio

    from ozonapi import SellerAPI, SellerAPIConfig

    async def get_product_info_limit():
        config = SellerAPIConfig(client_id="id", api_key="key")
        # config = SellerAPIConfig(token="token")

        async with SellerAPI(config=config) as api:
            return await api.product_info_limit()

    if __name__ == '__main__':
        limits = asyncio.run(get_product_info_limit())
"""
from .infrastructure import logging
from .infrastructure.logging import ozonapi_logger as logger
from .seller import SellerAPI, SellerAPIConfig


__version__ = "0.15.2"
__author__ = "Alexander Ulianov"
__email__ = "a.v.ulianov@mail.ru"
__repository__ = "https://github.com/a-ulianov/OzonAPI"
__docs__ = "https://github.com/a-ulianov/OzonAPI#readme"
__issues__ = "https://github.com/a-ulianov/OzonAPI/issues"

__all__ = ["SellerAPI", "SellerAPIConfig", "logging", "logger"]