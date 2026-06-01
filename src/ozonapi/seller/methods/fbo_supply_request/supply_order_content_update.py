from ...core import APIManager
from ...schemas.fbo_supply_request import (
    SupplyOrderContentUpdateRequest,
    SupplyOrderContentUpdateResponse,
)


class SupplyOrderContentUpdateMixin(APIManager):
    """Реализует метод /v1/supply-order/content/update"""

    async def supply_order_content_update(
            self: "SupplyOrderContentUpdateMixin",
            request: SupplyOrderContentUpdateRequest
    ) -> SupplyOrderContentUpdateResponse:
        """Запускает редактирование товарного состава заявки на поставку FBO.

        Notes:
            • Асинхронная операция; статус — через `supply_order_content_update_status()`
              по `operation_id`.
            • Перед применением нового состава его можно проверить методом
              `supply_order_content_update_validation()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SupplyOrderAPI_SupplyOrderContentUpdate

        Args:
            request: Запрос редактирования по схеме `SupplyOrderContentUpdateRequest`

        Returns:
            Идентификатор операции по схеме `SupplyOrderContentUpdateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_content_update(
                    SupplyOrderContentUpdateRequest(order_id=1, supply_id=2, items=[])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/content/update",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderContentUpdateResponse(**response)
