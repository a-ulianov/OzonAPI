from ...core import APIManager
from ...schemas.returns import (
    ReturnsRfbsReceiveReturnRequest,
    ReturnsRfbsReceiveReturnResponse,
)


class ReturnsRfbsReceiveReturnMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/receive-return"""

    async def returns_rfbs_receive_return(
            self: "ReturnsRfbsReceiveReturnMixin",
            request: ReturnsRfbsReceiveReturnRequest
    ) -> ReturnsRfbsReceiveReturnResponse:
        """Метод для подтверждения получения товара на проверку rFBS.

        Notes:
            • Подтверждает, что возвращённый покупателем товар получен продавцом на проверку.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsReceiveReturnV2

        Args:
            request: Запрос на подтверждение получения по схеме `ReturnsRfbsReceiveReturnRequest`

        Returns:
            Результат подтверждения по схеме `ReturnsRfbsReceiveReturnResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_receive_return(
                    ReturnsRfbsReceiveReturnRequest(
                        return_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/receive-return",
            payload=request.model_dump()
        )
        return ReturnsRfbsReceiveReturnResponse(**response)
