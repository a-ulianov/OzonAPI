"""
Получает список необработанных FBS/rFBS отправлений за указанный период времени (последние 30 дней)
и выводит детализированную информацию по каждому из них.
"""

import asyncio
import datetime
from pprint import pprint

from src.ozonapi import SellerAPI
from src.ozonapi.seller.schemas.fbs import PostingFBSGetRequest, PostingFBSUnfulfilledListRequest, \
    PostingFBSUnfulfilledListFilter


async def get_fbs_unfulfilled_postings_and_print_detailed_info():
    async with SellerAPI() as api:
        result = await api.posting_fbs_unfulfilled_list(
            PostingFBSUnfulfilledListRequest(
                filter=PostingFBSUnfulfilledListFilter(
                    delivering_date_from=datetime.datetime.now() - datetime.timedelta(days=30),
                    delivering_date_to=datetime.datetime.now(),
                ),
            )
        )

        for posting in result.result.postings:
            result = await api.posting_fbs_get(
                PostingFBSGetRequest(
                    posting_number=posting.posting_number
                )
            )
            pprint(result.model_dump())

if __name__ == '__main__':
    asyncio.run(get_fbs_unfulfilled_postings_and_print_detailed_info())