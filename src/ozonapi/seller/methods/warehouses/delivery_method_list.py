from ...core import APIManager
from ...schemas.warehouses import DeliveryMethodListRequest, DeliveryMethodListResponse


class DeliveryMethodListMixin(APIManager):
    """Реализует метод /v2/delivery-method/list"""

    async def delivery_method_list(
        self: "DeliveryMethodListMixin",
        request: DeliveryMethodListRequest = DeliveryMethodListRequest()
    ) -> DeliveryMethodListResponse:
        """Получает список методов доставки склада.

        Notes:
            • Для получения идентификатора склада используйте метод `warehouse_list()`.
            • Курсорная пагинация: если `has_next` равно true, передайте полученный `cursor`
              в следующий запрос, чтобы получить оставшиеся методы доставки.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_DeliveryMethodListV2

        Args:
            request: Фильтр и параметры пагинации по схеме `DeliveryMethodListRequest`.

        Returns:
            Список методов доставки с информацией о пагинации по схеме `DeliveryMethodListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_method_list(
                    DeliveryMethodListRequest(
                        filter=DeliveryMethodListFilter(
                            warehouse_ids=["15588127982000"],
                            status=[DeliveryMethodStatus.ACTIVE],
                        ),
                        limit=100,
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="delivery-method/list",
            payload=request.model_dump(),
        )
        return DeliveryMethodListResponse(**response)