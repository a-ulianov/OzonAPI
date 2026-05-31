from ...core import APIManager, method_rate_limit
from ...schemas import WarehouseListRequest
from ...schemas.warehouses import WarehouseListResponse


class WarehouseListMixin(APIManager):
    """Реализует метод /v2/warehouse/list"""

    @method_rate_limit(limit_requests=1, interval_seconds=60)
    async def warehouse_list(
        self: "WarehouseListMixin",
        request: WarehouseListRequest = WarehouseListRequest()
    ) -> WarehouseListResponse:
        """Возвращает список складов FBS и rFBS.

        Notes:
            • Чтобы получить список складов FBO, используйте метод `cluster_list()`.
            • Метод можно использовать `1` раз в минуту.
            • Курсорная пагинация: если `has_next` равно true, передайте полученный `cursor`
              в следующий запрос, чтобы получить оставшиеся склады.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_WarehouseListV2

        Args:
            request: Параметры запроса по схеме `WarehouseListRequest` (limit, cursor, warehouse_ids)

        Returns:
            Список складов FBS и rFBS с детальной информацией по схеме `WarehouseListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_list()
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="warehouse/list",
            payload=request.model_dump(),
        )
        return WarehouseListResponse(**response)
