from ...core import APIManager
from ...schemas.returns import ReturnsRfbsVerifyRequest, ReturnsRfbsVerifyResponse


class ReturnsRfbsVerifyMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/verify"""

    async def returns_rfbs_verify(
            self: "ReturnsRfbsVerifyMixin",
            request: ReturnsRfbsVerifyRequest
    ) -> ReturnsRfbsVerifyResponse:
        """Метод для одобрения заявки на возврат rFBS.

        Notes:
            • Одобряет заявку; можно указать способ возврата товара.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsVerifyV2

        Args:
            request: Запрос на одобрение заявки по схеме `ReturnsRfbsVerifyRequest`

        Returns:
            Результат одобрения заявки по схеме `ReturnsRfbsVerifyResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_verify(
                    ReturnsRfbsVerifyRequest(
                        return_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/verify",
            payload=request.model_dump()
        )
        return ReturnsRfbsVerifyResponse(**response)
