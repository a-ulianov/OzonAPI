from ..core import APIManager, method_rate_limit
from ..schemas.warehouses import WarehouseListResponse
from ..schemas.warehouses import DeliveryMethodListRequest, DeliveryMethodListResponse


class SellerWarehouseAPI(APIManager):
    """Реализует методы раздела Склады.

    References:
        https://docs.ozon.ru/api/seller/#tag/WarehouseAPI
    """

    @method_rate_limit(limit_requests=1, interval_seconds=60)
    async def warehouse_list(
        self: "SellerWarehouseAPI"
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

    async def delivery_method_list(
        self: "SellerWarehouseAPI",
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
            json=request.model_dump(),
        )
        return DeliveryMethodListResponse(**response)