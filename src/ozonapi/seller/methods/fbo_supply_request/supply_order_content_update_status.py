from ...core import APIManager
from ...schemas.fbo_supply_request import (
    SupplyOrderContentUpdateStatusRequest,
    SupplyOrderContentUpdateStatusResponse,
)


class SupplyOrderContentUpdateStatusMixin(APIManager):
    """Реализует метод /v1/supply-order/content/update/status"""

    async def supply_order_content_update_status(
            self: "SupplyOrderContentUpdateStatusMixin",
            request: SupplyOrderContentUpdateStatusRequest
    ) -> SupplyOrderContentUpdateStatusResponse:
        """Возвращает статус редактирования товарного состава заявки на поставку FBO.

        Notes:
            • Используйте `operation_id`, полученный методом
              `supply_order_content_update()`.
            • При успехе возвращается `new_bundle_id` — идентификатор нового состава.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderContentUpdateStatus

        Args:
            request: Запрос статуса по схеме `SupplyOrderContentUpdateStatusRequest`

        Returns:
            Статус редактирования по схеме `SupplyOrderContentUpdateStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_content_update_status(
                    SupplyOrderContentUpdateStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/content/update/status",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderContentUpdateStatusResponse(**response)
