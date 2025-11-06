import asyncio
from pprint import pprint

from src.ozonapi import SellerAPI
from src.ozonapi.seller.schemas.entities.postings import PostingFilterWith
from src.ozonapi.seller.schemas.fbo import PostingFBOGetRequest


async def get_posting_fbo_detailed(posting_number: str):
    # OZON_SELLER_TOKEN или OZON_SELLER_CLIENT_ID + OZON_SELLER_API_KEY определены в .env
    async with SellerAPI() as api:
        # noinspection PyArgumentList
        result = await api.posting_fbo_get(
            PostingFBOGetRequest(
                posting_number=posting_number,
                translit=False,
                with_=PostingFilterWith(
                    analytics_data=True,
                    financial_data=False,
                    legal_info=True
                )
            )
        )
        pprint(result.model_dump())


if __name__ == '__main__':
    posting_number = "35880011-0171-1"
    asyncio.run(get_posting_fbo_detailed(posting_number))