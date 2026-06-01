from ...core import APIManager
from ...schemas.warehouses import WarehouseWithInvalidProductsResponse


class WarehouseWarehousesWithInvalidProductsMixin(APIManager):
    """Реализует метод /v1/warehouse/warehouses-with-invalid-products"""

    async def warehouse_warehouses_with_invalid_products(
            self: "WarehouseWarehousesWithInvalidProductsMixin"
    ) -> WarehouseWithInvalidProductsResponse:
        """Возвращает список складов с ограниченными для доставки товарами.

        Notes:
            • Запрос без тела.
            • Детали ограничений по складу — методом `warehouse_invalid_products_get()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseWithInvalidProducts

        Returns:
            Идентификаторы складов по схеме `WarehouseWithInvalidProductsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_warehouses_with_invalid_products()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/warehouses-with-invalid-products",
            payload={}
        )
        return WarehouseWithInvalidProductsResponse(**response)
