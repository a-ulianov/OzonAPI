from ...core import APIManager, method_rate_limit
from ...schemas.warehouses import WarehouseListResponse


class WarehouseListMixin(APIManager):
    """Реализует метод /v1/warehouse/list"""

    @method_rate_limit(limit_requests=1, interval_seconds=60)
    async def warehouse_list(
        self: "WarehouseListMixin"
    ) -> WarehouseListResponse:
        """Возвращает список складов FBS и rFBS.

        Notes:
            • Чтобы получить список складов FBO, используйте метод `cluster_list()`.
            • Метод можно использовать `1` раз в минуту.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/WarehouseAPI_WarehouseList

        Returns:
            Список складов FBS и rFBS с детальной информацией по схеме `WarehouseListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/list",
        )
        return WarehouseListResponse(**response)
