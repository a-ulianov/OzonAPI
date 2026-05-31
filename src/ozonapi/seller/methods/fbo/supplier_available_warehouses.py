from ...core import APIManager
from ...schemas.fbo import SupplierAvailableWarehousesResponse


class SupplierAvailableWarehousesMixin(APIManager):
    """Реализует метод /v1/supplier/available_warehouses"""

    async def supplier_available_warehouses(
            self: "SupplierAvailableWarehousesMixin",
    ) -> SupplierAvailableWarehousesResponse:
        """Метод для получения информации о загруженности складов Ozon.

        Notes:
            • Эндпоинт использует HTTP-метод GET (без тела запроса).
            • Помогает выбрать менее загруженный склад при планировании поставки.

        References:
            https://docs.ozon.com/api/seller/?#operation/WarehouseAPI_AvailableWarehouses

        Returns:
            Загруженность складов Ozon по схеме `SupplierAvailableWarehousesResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supplier_available_warehouses()
        """
        response = await self._request(
            method="get",
            api_version="v1",
            endpoint="supplier/available_warehouses",
        )
        return SupplierAvailableWarehousesResponse(**response)
