from ...core import APIManager
from ...schemas.returns import (
    ReturnsRfbsCompensateRequest,
    ReturnsRfbsCompensateResponse,
)


class ReturnsRfbsCompensateMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/compensate"""

    async def returns_rfbs_compensate(
            self: "ReturnsRfbsCompensateMixin",
            request: ReturnsRfbsCompensateRequest
    ) -> ReturnsRfbsCompensateResponse:
        """Метод для возврата части стоимости товара rFBS.

        Notes:
            • Компенсирует покупателю часть стоимости товара без его возврата.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsCompensateV2

        Args:
            request: Запрос на компенсацию по схеме `ReturnsRfbsCompensateRequest`

        Returns:
            Результат компенсации по схеме `ReturnsRfbsCompensateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_compensate(
                    ReturnsRfbsCompensateRequest(
                        return_id=12345,
                        compensation_amount="100"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/compensate",
            payload=request.model_dump()
        )
        return ReturnsRfbsCompensateResponse(**response)
