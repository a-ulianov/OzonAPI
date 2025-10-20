import asyncio
import datetime

from src.ozonapi import SellerAPI
from src.ozonapi.seller.schemas.fbs import PostingFBSGetRequest, PostingFBSUnfulfilledListRequest, \
    PostingFBSUnfulfilledListFilter


async def main():
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
            print(result)

if __name__ == '__main__':
    asyncio.run(main())