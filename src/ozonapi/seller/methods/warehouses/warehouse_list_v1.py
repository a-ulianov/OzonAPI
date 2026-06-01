from ...core import APIManager
from ...schemas.warehouses import WarehouseListV1Request, WarehouseListV1Response


class WarehouseListV1Mixin(APIManager):
    """Реализует метод /v1/warehouse/list"""

    async def warehouse_list_v1(
            self: "WarehouseListV1Mixin",
            request: WarehouseListV1Request = WarehouseListV1Request()
    ) -> WarehouseListV1Response:
        """Возвращает список складов FBS и rFBS (устаревшая версия 1).

        Notes:
            • Постраничная выдача через `limit`/`offset`.
            • Рекомендуется использовать `warehouse_list()` (v2, курсорная пагинация).

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_WarehouseList

        Args:
            request: Параметры запроса по схеме `WarehouseListV1Request`

        Returns:
            Список складов по схеме `WarehouseListV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_list_v1()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseListV1Response(**response)
