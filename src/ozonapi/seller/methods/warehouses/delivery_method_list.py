from ...core import APIManager
from ...schemas.warehouses import DeliveryMethodListRequest, DeliveryMethodListResponse


class DeliveryMethodListMixin(APIManager):
    """Реализует метод /v1/delivery-method/list"""

    async def delivery_method_list(
        self: "DeliveryMethodListMixin",
        request: DeliveryMethodListRequest = DeliveryMethodListRequest()
    ) -> DeliveryMethodListResponse:
        """Получает список методов доставки склада.

        Notes:
            • Для получения идентификатора склада используйте метод `warehouse_list()`.
            • В ответе может быть только часть методов доставки - используйте параметр `offset` в запросе и `has_next` из ответа для пагинации.
            • Максимальное количество элементов в ответе - `50`.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/WarehouseAPI_DeliveryMethodList

        Args:
            request: Фильтр и параметры пагинации для получения методов доставки по схеме `DeliveryMethodListRequest`.

        Returns:
            Список методов доставки с информацией о пагинации по схеме `DeliveryMethodListResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_method_list(
                    DeliveryMethodListRequest(
                        filter=DeliveryMethodListRequestFilter(
                            provider_id=424,
                            status=DeliveryMethodStatus.ACTIVE,
                            warehouse_id=15588127982000
                        ),
                        limit=50,
                        offset=0
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery-method/list",
            payload=request.model_dump(),
        )
        return DeliveryMethodListResponse(**response)