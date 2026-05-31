from ...core import APIManager
from ...schemas.fbo import SupplyOrderListRequest, SupplyOrderListResponse


class SupplyOrderListMixin(APIManager):
    """Реализует метод /v3/supply-order/list"""

    async def supply_order_list(
            self: "SupplyOrderListMixin",
            request: SupplyOrderListRequest
    ) -> SupplyOrderListResponse:
        """Метод для получения списка заявок на поставку на склад Ozon.

        Notes:
            • Метод возвращает только идентификаторы заявок; подробности получайте
              методом `supply_order_get`.
            • Фильтр по статусам (`filter.states`) обязателен.
            • Для пагинации используйте `limit` и `last_id` (берётся из ответа).
            • Сортировку задают параметры `sort_by` и `sort_dir`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderListV3

        Args:
            request: Запрос на получение списка заявок на поставку по схеме `SupplyOrderListRequest`

        Returns:
            Список идентификаторов заявок на поставку по схеме `SupplyOrderListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_list(
                    SupplyOrderListRequest(
                        filter=SupplyOrderListFilter(
                            states=[SupplyOrderState.READY_TO_SUPPLY],
                        ),
                        limit=100,
                        sort_by=SupplyOrderSortField.ORDER_CREATION,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="supply-order/list",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderListResponse(**response)
