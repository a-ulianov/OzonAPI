from ...core import APIManager
from ...schemas.returns import (
    ReturnsRfbsReturnMoneyRequest,
    ReturnsRfbsReturnMoneyResponse,
)


class ReturnsRfbsReturnMoneyMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/return-money"""

    async def returns_rfbs_return_money(
            self: "ReturnsRfbsReturnMoneyMixin",
            request: ReturnsRfbsReturnMoneyRequest
    ) -> ReturnsRfbsReturnMoneyResponse:
        """Метод для возврата денег покупателю rFBS.

        Notes:
            • Возвращает покупателю деньги; можно указать сумму за пересылку.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsReturnMoneyV2

        Args:
            request: Запрос на возврат денег по схеме `ReturnsRfbsReturnMoneyRequest`

        Returns:
            Результат возврата денег по схеме `ReturnsRfbsReturnMoneyResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_return_money(
                    ReturnsRfbsReturnMoneyRequest(
                        return_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/return-money",
            payload=request.model_dump()
        )
        return ReturnsRfbsReturnMoneyResponse(**response)
