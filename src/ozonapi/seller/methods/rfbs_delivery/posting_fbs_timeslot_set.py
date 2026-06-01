from ...core import APIManager
from ...schemas.rfbs_delivery import (
    PostingFbsTimeslotSetRequest,
    PostingFbsTimeslotSetResponse,
)


class PostingFbsTimeslotSetMixin(APIManager):
    """Реализует метод /v1/posting/fbs/timeslot/set"""

    async def posting_fbs_timeslot_set(
            self: "PostingFbsTimeslotSetMixin",
            request: PostingFbsTimeslotSetRequest
    ) -> PostingFbsTimeslotSetResponse:
        """Переносит дату доставки отправления rFBS.

        Notes:
            • Доступные интервалы — методом `posting_fbs_timeslot_change_restrictions()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_SetPostingTimeslot

        Args:
            request: Запрос переноса по схеме `PostingFbsTimeslotSetRequest`

        Returns:
            Результат переноса по схеме `PostingFbsTimeslotSetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_timeslot_set(
                    PostingFbsTimeslotSetRequest(posting_number="123-456-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/timeslot/set",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFbsTimeslotSetResponse(**response)
