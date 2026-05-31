from ...core import APIManager
from ...schemas.returns import ReturnsRfbsListRequest, ReturnsRfbsListResponse


class ReturnsRfbsListMixin(APIManager):
    """Реализует метод /v2/returns/rfbs/list"""

    async def returns_rfbs_list(
            self: "ReturnsRfbsListMixin",
            request: ReturnsRfbsListRequest
    ) -> ReturnsRfbsListResponse:
        """Метод для получения списка заявок на возврат rFBS.

        Notes:
            • Возвращает заявки на возврат с фильтрацией по товару, отправлению, статусам и дате.
            • Постраничный вывод через `limit` и `last_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsRfbsListV2

        Args:
            request: Запрос на получение списка заявок по схеме `ReturnsRfbsListRequest`

        Returns:
            Список заявок на возврат по схеме `ReturnsRfbsListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_rfbs_list(
                    ReturnsRfbsListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/list",
            payload=request.model_dump()
        )
        return ReturnsRfbsListResponse(**response)
