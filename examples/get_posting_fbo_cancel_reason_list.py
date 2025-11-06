import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI


async def get_posting_fbo_cancel_reason_list():
    """Получает и выводит список доступных причин отмены отправлений FBO."""
    async with SellerAPI() as api:
        result = await api.posting_fbo_cancel_reason_list()
        pprint(result.model_dump())

if __name__ == '__main__':
    asyncio.run(get_posting_fbo_cancel_reason_list())