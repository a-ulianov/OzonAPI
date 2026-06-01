from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseOzonListRequest,
    WarehouseOzonListResponse,
)


class WarehouseOzonListMixin(APIManager):
    """Реализует метод /v1/warehouse/ozon/list"""

    async def warehouse_ozon_list(
            self: "WarehouseOzonListMixin",
            request: WarehouseOzonListRequest
    ) -> WarehouseOzonListResponse:
        """Возвращает список складов Ozon (FBO).

        Notes:
            • Фильтрация по типам складов через `warehouse_types`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseOZONList

        Args:
            request: Запрос по схеме `WarehouseOzonListRequest`

        Returns:
            Список складов Ozon по схеме `WarehouseOzonListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_ozon_list(
                    WarehouseOzonListRequest(warehouse_types=["FULL_FILLMENT"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/ozon/list",
            payload=request.model_dump()
        )
        return WarehouseOzonListResponse(**response)
