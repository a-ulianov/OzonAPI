from ...core import APIManager
from ...schemas.fbo import SupplyOrderPassStatusRequest, SupplyOrderPassStatusResponse


class SupplyOrderPassStatusMixin(APIManager):
    """Реализует метод /v1/supply-order/pass/status"""

    async def supply_order_pass_status(
            self: "SupplyOrderPassStatusMixin",
            request: SupplyOrderPassStatusRequest
    ) -> SupplyOrderPassStatusResponse:
        """Метод для получения статуса ввода данных о водителе и автомобиле.

        Notes:
            • Используется вместе с `supply_order_pass_create`: передайте полученный
              `operation_id` для проверки результата операции.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderPassStatus

        Args:
            request: Запрос на получение статуса ввода данных по схеме `SupplyOrderPassStatusRequest`

        Returns:
            Статус ввода данных о водителе и автомобиле по схеме `SupplyOrderPassStatusResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_pass_status(
                    SupplyOrderPassStatusRequest(operation_id="operation-id")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/pass/status",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderPassStatusResponse(**response)
