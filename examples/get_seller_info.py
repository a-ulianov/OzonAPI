import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig


async def get_product_info_limit():
    """
    Получает и выводит информацию о продавце, рейтингах и подписке.

    client_id и api_key определены в .env с префиксом OZON_SELLER_:
    OZON_SELLER_CLIENT_ID=...
    OZON_SELLER_API_KEY=...
    """

    async with SellerAPI() as api:
        result = await api.seller_info()

        # Выводим в консоль, предварительно преобразовав ответ в словарь (для наглядности)
        pprint(result.model_dump())

if __name__ == '__main__':
    asyncio.run(get_product_info_limit())