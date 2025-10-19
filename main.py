import asyncio
import datetime

from src.ozonapi import SellerAPI
from src.ozonapi.seller.schemas.fbs import PostingFBSListRequest, PostingFBSListFilter, \
    PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate, PostingFBSUnfulfilledListRequest, \
    PostingFBSUnfulfilledListFilter


async def main() -> None:

    # filter_obj = PostingFBSUnfulfilledListRequestFilterLastChangedStatusDate(
    #     from_=datetime.datetime.now() - datetime.timedelta(days=30),
    #     to_=datetime.datetime.now(),
    # )
    # print("Filter dump:", filter_obj.model_dump(by_alias=True))

    # filter_obj = PostingFBSListFilter(
    #     since=datetime.datetime.now() - datetime.timedelta(days=30),
    #     to_=datetime.datetime.now(),
    # )
    # print("Filter dump:", filter_obj.model_dump(by_alias=True))

    async with SellerAPI() as api:
        # noinspection PyArgumentList

        result = await api.posting_fbs_unfulfilled_list(
            PostingFBSUnfulfilledListRequest(
                filter=PostingFBSUnfulfilledListFilter(
                    delivering_date_from=datetime.datetime.now() - datetime.timedelta(days=30),
                    delivering_date_to=datetime.datetime.now(),
                ),
            )
        )
        print(result)

if __name__ == "__main__":
    asyncio.run(main())