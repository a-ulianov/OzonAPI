from ...core import APIManager
from ...schemas.rfbs_delivery import (
    FbsPostingMoveStatusResponse,
    FbsPostingTrackingNumberSetRequest,
)


class FbsPostingTrackingNumberSetMixin(APIManager):
    """Реализует метод /v2/fbs/posting/tracking-number/set"""

    async def fbs_posting_tracking_number_set(
            self: "FbsPostingTrackingNumberSetMixin",
            request: FbsPostingTrackingNumberSetRequest
    ) -> FbsPostingMoveStatusResponse:
        """Добавляет трек-номера к отправлениям rFBS.

        Notes:
            • В ответе по каждому отправлению возвращается признак `result`
              и текст ошибки `error` при неудаче.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingTrackingNumberSet

        Args:
            request: Запрос трек-номеров по схеме `FbsPostingTrackingNumberSetRequest`

        Returns:
            Результаты по каждому отправлению по схеме `FbsPostingMoveStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_tracking_number_set(
                    FbsPostingTrackingNumberSetRequest(tracking_numbers=[])
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="fbs/posting/tracking-number/set",
            payload=request.model_dump(by_alias=True)
        )
        return FbsPostingMoveStatusResponse(**response)
