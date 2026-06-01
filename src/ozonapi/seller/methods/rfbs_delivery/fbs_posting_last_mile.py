from ...core import APIManager
from ...schemas.rfbs_delivery import (
    FbsPostingMoveStatusResponse,
    FbsPostingNumbersRequest,
)


class FbsPostingLastMileMixin(APIManager):
    """Реализует метод /v2/fbs/posting/last-mile"""

    async def fbs_posting_last_mile(
            self: "FbsPostingLastMileMixin",
            request: FbsPostingNumbersRequest
    ) -> FbsPostingMoveStatusResponse:
        """Переводит отправления rFBS в статус «Последняя миля».

        Notes:
            • В ответе по каждому отправлению возвращается признак `result`
              и текст ошибки `error` при неудаче.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingLastMile

        Args:
            request: Номера отправлений по схеме `FbsPostingNumbersRequest`

        Returns:
            Результаты по каждому отправлению по схеме `FbsPostingMoveStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_last_mile(
                    FbsPostingNumbersRequest(posting_number=["123-456-1"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="fbs/posting/last-mile",
            payload=request.model_dump(by_alias=True)
        )
        return FbsPostingMoveStatusResponse(**response)
