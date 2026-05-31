from ...core import APIManager
from ...schemas.returns import ReturnsRfbsRejectRequest, ReturnsRfbsRejectResponse


class ReturnsRfbsRejectMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/reject"""

    async def returns_rfbs_reject(
            self: "ReturnsRfbsRejectMixin",
            request: ReturnsRfbsRejectRequest
    ) -> ReturnsRfbsRejectResponse:
        """Метод для отклонения заявки на возврат rFBS.

        Notes:
            • Отклоняет заявку по указанной причине; для части причин обязателен комментарий.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsRejectV2

        Args:
            request: Запрос на отклонение заявки по схеме `ReturnsRfbsRejectRequest`

        Returns:
            Результат отклонения заявки по схеме `ReturnsRfbsRejectResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_reject(
                    ReturnsRfbsRejectRequest(
                        return_id=12345,
                        rejection_reason_id=1
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/reject",
            payload=request.model_dump()
        )
        return ReturnsRfbsRejectResponse(**response)
