from ...core import APIManager
from ...schemas.returns import ReturnsListRequest, ReturnsListResponse


class ReturnsListMixin(APIManager):
    """Реализует метод /v1/returns/list"""

    async def returns_list(
            self: "ReturnsListMixin",
            request: ReturnsListRequest
    ) -> ReturnsListResponse:
        """Метод для получения информации о возвратах FBO и FBS.

        Notes:
            • Возвращает список возвратов с фильтрацией по датам, заказам, товарам, складу и статусам.
            • Постраничный вывод через `limit` и `last_id` (идентификатор последнего возврата).

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_GetReturnsList

        Args:
            request: Запрос на получение списка возвратов по схеме `ReturnsListRequest`

        Returns:
            Информация о возвратах по схеме `ReturnsListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_list(
                    ReturnsListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="returns/list",
            payload=request.model_dump()
        )
        return ReturnsListResponse(**response)
