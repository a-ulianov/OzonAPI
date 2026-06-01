from ...core import APIManager
from ...schemas.polygons import PolygonBindRequest, PolygonBindResponse


class PolygonBindMixin(APIManager):
    """Реализует метод /v2/polygon/bind"""

    async def polygon_bind(
            self: "PolygonBindMixin",
            request: PolygonBindRequest,
    ) -> PolygonBindResponse:
        """Связывает метод доставки с полигоном доставки.

        Notes:
            • Канонический метод привязки полигона (v2). Устаревшая версия v1
              доступна как `polygon_bind_v1()`.
            • Время доставки `time` ограничено набором: 15, 30, 45, 60, 90, 120, 150
              минут (перечисление `PolygonDeliveryTime`).
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonBind

        Args:
            request: Параметры привязки полигона по схеме `PolygonBindRequest`

        Returns:
            Пустой ответ по схеме `PolygonBindResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.polygon_bind(
                    PolygonBindRequest(
                        delivery_method_id=123,
                        polygon_id=456,
                        time=PolygonDeliveryTime.MIN_30,
                        warehouse_id=789,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="polygon/bind",
            payload=request.model_dump(),
        )
        return PolygonBindResponse(**response)
