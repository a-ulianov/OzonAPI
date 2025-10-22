import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig
from src.ozonapi.seller.schemas.fbs import PostingFBSProductCountryListRequest


async def get_posting_fbs_product_country_list():
    """
    Получает и выводит список доступных стран-изготовителей и их ISO кодов.

    client_id и api_key определены в .env с префиксом OZON_SELLER_:
    OZON_SELLER_CLIENT_ID=...
    OZON_SELLER_API_KEY=...
    """
    async with SellerAPI(
            # Понижаем уровень логирования (для наглядности)
            config=SellerAPIConfig(log_level="DEBUG")
    ) as api:
        result = await api.posting_fbs_product_country_list(
            PostingFBSProductCountryListRequest(
                name_search="тУрЦ",
            )
        )

        # Выводим в консоль, предварительно преобразовав ответ в словарь (для наглядности)
        pprint(result.model_dump())

if __name__ == '__main__':
    asyncio.run(get_posting_fbs_product_country_list())
