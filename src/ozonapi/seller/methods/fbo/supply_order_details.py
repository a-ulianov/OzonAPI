from ...core import APIManager
from ...schemas.fbo import SupplyOrderDetailsRequest, SupplyOrderDetailsResponse


class SupplyOrderDetailsMixin(APIManager):
    """Реализует метод /v1/supply-order/details"""

    async def supply_order_details(
            self: "SupplyOrderDetailsMixin",
            request: SupplyOrderDetailsRequest
    ) -> SupplyOrderDetailsResponse:
        """Метод для получения подробной информации о заявке на поставку.

        Notes:
            • Возвращает расширенные данные: возможность изменения интервала, состава,
              данных о водителе и автомобиле, а также теги и статусы поставок.
            • Идентификатор заявки (`order_id`) получают методом `supply_order_list`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_GetSupplyOrderDetails

        Args:
            request: Запрос на получение подробной информации по схеме `SupplyOrderDetailsRequest`

        Returns:
            Подробная информация о заявке на поставку по схеме `SupplyOrderDetailsResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_details(
                    SupplyOrderDetailsRequest(order_id=1234567890)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/details",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderDetailsResponse(**response)
