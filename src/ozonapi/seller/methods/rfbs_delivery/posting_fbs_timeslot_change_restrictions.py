from ...core import APIManager
from ...schemas.rfbs_delivery import (
    PostingFbsTimeslotChangeRestrictionsRequest,
    PostingFbsTimeslotChangeRestrictionsResponse,
)


class PostingFbsTimeslotChangeRestrictionsMixin(APIManager):
    """Реализует метод /v1/posting/fbs/timeslot/change-restrictions"""

    async def posting_fbs_timeslot_change_restrictions(
            self: "PostingFbsTimeslotChangeRestrictionsMixin",
            request: PostingFbsTimeslotChangeRestrictionsRequest
    ) -> PostingFbsTimeslotChangeRestrictionsResponse:
        """Возвращает доступные даты для переноса доставки отправления rFBS.

        Notes:
            • Возвращает допустимый интервал доставки и оставшееся число переносов.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingTimeslotChangeRestrictions

        Args:
            request: Запрос по схеме `PostingFbsTimeslotChangeRestrictionsRequest`

        Returns:
            Доступные даты по схеме `PostingFbsTimeslotChangeRestrictionsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_timeslot_change_restrictions(
                    PostingFbsTimeslotChangeRestrictionsRequest(posting_number="123-456-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/timeslot/change-restrictions",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFbsTimeslotChangeRestrictionsResponse(**response)
