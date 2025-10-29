import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI, SellerAPIConfig


async def get_posting_fbs_cancel_reason_list():
    """Получает и выводит список доступных причин отмены отправлений FBS."""
    async with SellerAPI(config=SellerAPIConfig(log_level="DEBUG")) as api:
        result = await api.posting_fbs_cancel_reason_list()
        pprint(result)

if __name__ == '__main__':
    asyncio.run(get_posting_fbs_cancel_reason_list())