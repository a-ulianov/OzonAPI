from ...core import APIManager
from ...schemas.fbo import SupplyOrderGetRequest, SupplyOrderGetResponse


class SupplyOrderGetMixin(APIManager):
    """Реализует метод /v3/supply-order/get"""

    async def supply_order_get(
            self: "SupplyOrderGetMixin",
            request: SupplyOrderGetRequest
    ) -> SupplyOrderGetResponse:
        """Метод для получения информации о заявках на поставку по их идентификаторам.

        Notes:
            • Идентификаторы заявок (`order_ids`) получают методом `supply_order_list`.
            • Ответ содержит подробную информацию: статус, пункт отгрузки, поставки,
              интервал поставки, теги заявки.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderV3

        Args:
            request: Запрос на получение информации о заявках по схеме `SupplyOrderGetRequest`

        Returns:
            Информация о заявках на поставку по схеме `SupplyOrderGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_get(
                    SupplyOrderGetRequest(order_ids=[1234567890])
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="supply-order/get",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderGetResponse(**response)
