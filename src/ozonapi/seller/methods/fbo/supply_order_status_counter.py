from ...core import APIManager
from ...schemas.fbo import SupplyOrderStatusCounterResponse


class SupplyOrderStatusCounterMixin(APIManager):
    """Реализует метод /v1/supply-order/status/counter"""

    async def supply_order_status_counter(
            self: "SupplyOrderStatusCounterMixin",
    ) -> SupplyOrderStatusCounterResponse:
        """Метод для получения количества заявок на поставку, сгруппированного по статусам.

        Notes:
            • Метод не принимает параметров и возвращает счётчики по всем статусам заявок.
            • Используйте результат для быстрой навигации по статусам перед запросом списка заявок.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderStatusCounter

        Returns:
            Количество заявок на поставку по статусам по схеме `SupplyOrderStatusCounterResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_status_counter()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/status/counter",
        )
        return SupplyOrderStatusCounterResponse(**response)
