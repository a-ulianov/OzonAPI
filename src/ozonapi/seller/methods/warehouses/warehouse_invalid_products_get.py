from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseInvalidProductsGetRequest,
    WarehouseInvalidProductsGetResponse,
)


class WarehouseInvalidProductsGetMixin(APIManager):
    """Реализует метод /v1/warehouse/invalid-products/get"""

    async def warehouse_invalid_products_get(
            self: "WarehouseInvalidProductsGetMixin",
            request: WarehouseInvalidProductsGetRequest
    ) -> WarehouseInvalidProductsGetResponse:
        """Возвращает список товаров с ограничениями по доставке для склада.

        Notes:
            • Пагинация по `last_id`: при `has_next` равном true передайте полученный
              `last_id` в следующий запрос.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseInvalidProductsGet

        Args:
            request: Запрос по схеме `WarehouseInvalidProductsGetRequest`

        Returns:
            Товары с ограничениями по схеме `WarehouseInvalidProductsGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_invalid_products_get(
                    WarehouseInvalidProductsGetRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/invalid-products/get",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseInvalidProductsGetResponse(**response)
