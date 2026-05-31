from ...core import APIManager
from ...schemas.fbo import SupplyOrderBundleRequest, SupplyOrderBundleResponse


class SupplyOrderBundleMixin(APIManager):
    """Реализует метод /v1/supply-order/bundle"""

    async def supply_order_bundle(
            self: "SupplyOrderBundleMixin",
            request: SupplyOrderBundleRequest
    ) -> SupplyOrderBundleResponse:
        """Метод для получения состава поставки или заявки на поставку.

        Notes:
            • Возвращает список товаров, входящих в указанные составы (бандлы).
            • Для пагинации используйте `limit` и `last_id` (берётся из ответа).
            • Сортировку задают параметры `sort_field` и `is_asc`.
            • Теги товаров рассчитываются при передаче `item_tags_calculation`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderBundle

        Args:
            request: Запрос на получение состава поставки по схеме `SupplyOrderBundleRequest`

        Returns:
            Состав поставки или заявки на поставку по схеме `SupplyOrderBundleResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_bundle(
                    SupplyOrderBundleRequest(
                        bundle_ids=["1234567890"],
                        limit=100,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/bundle",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderBundleResponse(**response)
