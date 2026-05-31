from ...core import APIManager
from ...schemas.returns import ReturnsRfbsGetRequest, ReturnsRfbsGetResponse


class ReturnsRfbsGetMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/get"""

    async def returns_rfbs_get(
            self: "ReturnsRfbsGetMixin",
            request: ReturnsRfbsGetRequest
    ) -> ReturnsRfbsGetResponse:
        """Метод для получения информации о заявке на возврат rFBS.

        Notes:
            • Возвращает подробную информацию о заявке: товар, причину, статус,
              доступные действия и способ возврата.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsGetV2

        Args:
            request: Запрос на получение информации о заявке по схеме `ReturnsRfbsGetRequest`

        Returns:
            Информация о заявке на возврат по схеме `ReturnsRfbsGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_get(
                    ReturnsRfbsGetRequest(
                        return_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/get",
            payload=request.model_dump()
        )
        return ReturnsRfbsGetResponse(**response)
