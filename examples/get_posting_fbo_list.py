import asyncio
import datetime
from pprint import pprint

from src.ozonapi import SellerAPI
from src.ozonapi.seller.common.enumerations.postings import PostingStatus
from src.ozonapi.seller.common.enumerations.requests import SortingDirection
from src.ozonapi.seller.schemas.entities.postings import PostingFilter, PostingFilterWith
from src.ozonapi.seller.schemas.fbo import PostingFBOListRequest


async def main():
    # OZON_SELLER_TOKEN или OZON_SELLER_CLIENT_ID + OZON_SELLER_API_KEY определены в .env
    async with SellerAPI() as api:
        # noinspection PyArgumentList
        result = await api.posting_fbo_list(
            PostingFBOListRequest(
                dir=SortingDirection.ASC,
                filter=PostingFilter(
                    since=datetime.datetime.now() - datetime.timedelta(days=30),
                    to=datetime.datetime.now(),
                    status=PostingStatus.DELIVERED
                ),
                limit=100,
                offset=0,
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
    asyncio.run(main())