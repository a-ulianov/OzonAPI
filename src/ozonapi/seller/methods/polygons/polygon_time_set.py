from ...core import APIManager
from ...schemas.polygons import PolygonTimeSetRequest, PolygonTimeSetResponse


class PolygonTimeSetMixin(APIManager):
    """Реализует метод /v1/polygon/time/set"""

    async def polygon_time_set(
            self: "PolygonTimeSetMixin",
            request: PolygonTimeSetRequest,
    ) -> PolygonTimeSetResponse:
        """Устанавливает новое время доставки в полигоне.

        Notes:
            • Меняет время доставки полигона с `current_time` на `new_time`.
            • Допустимые значения времени: 15, 30, 45, 60, 90, 120, 150 минут
              (перечисление `PolygonDeliveryTime`).
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonTimeSet

        Args:
            request: Параметры изменения времени по схеме `PolygonTimeSetRequest`

        Returns:
            Пустой ответ по схеме `PolygonTimeSetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.polygon_time_set(
                    PolygonTimeSetRequest(
                        current_time=PolygonDeliveryTime.MIN_30,
                        new_time=PolygonDeliveryTime.MIN_60,
                        delivery_method_id=123,
                        polygon_id=456,
                        warehouse_id=789,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="polygon/time/set",
            payload=request.model_dump(),
        )
        return PolygonTimeSetResponse(**response)
