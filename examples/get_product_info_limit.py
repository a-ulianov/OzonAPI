import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig


async def get_product_info_limit():
    """
    Получает и выводит информацию о лимитах на ассортимент, создание и обновление товаров.

    client_id и api_key определены в .env с префиксом OZON_SELLER_:
    OZON_SELLER_CLIENT_ID=...
    OZON_SELLER_API_KEY=...
    """

    async with SellerAPI(
            # Понижаем уровень логирования (для наглядности)
            config=SellerAPIConfig(log_level="DEBUG")
    ) as api:
        result = await api.product_info_limit()

        # Выводим в консоль, предварительно преобразовав ответ в словарь (для наглядности)
        pprint(result.model_dump())

if __name__ == '__main__':
    asyncio.run(get_product_info_limit())
