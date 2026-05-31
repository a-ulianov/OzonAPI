from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSTraceableSplitRequest,
    PostingFBSTraceableSplitResponse,
)


class PostingFBSTraceableSplitMixin(APIManager):
    """Реализует метод /v1/posting/fbs/traceable/split"""

    async def posting_fbs_traceable_split(
            self: "PostingFBSTraceableSplitMixin",
            request: PostingFBSTraceableSplitRequest
    ) -> PostingFBSTraceableSplitResponse:
        """Метод для разделения отправления с прослеживаемыми товарами.

        Notes:
            • Делит отправление так, чтобы прослеживаемые товары попали в отдельные отправления.
            • В ответе указывается признак `potential_blr_traceable` для каждого отправления.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFbsTraceableSplit

        Args:
            request: Запрос на разделение отправления по схеме `PostingFBSTraceableSplitRequest`

        Returns:
            Результат разделения отправления по схеме `PostingFBSTraceableSplitResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_traceable_split(
                    PostingFBSTraceableSplitRequest(
                        posting_number="33920113-1231-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/traceable/split",
            payload=request.model_dump()
        )
        return PostingFBSTraceableSplitResponse(**response)
