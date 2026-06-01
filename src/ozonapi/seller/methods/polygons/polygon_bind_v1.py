from ...core import APIManager
from ...schemas.polygons import PolygonBindV1Request, PolygonBindV1Response


class PolygonBindV1Mixin(APIManager):
    """Реализует метод /v1/polygon/bind"""

    async def polygon_bind_v1(
            self: "PolygonBindV1Mixin",
            request: PolygonBindV1Request,
    ) -> PolygonBindV1Response:
        """Связывает метод доставки с полигонами доставки (устаревшая версия v1).

        Notes:
            • Устаревшая версия метода привязки. Предпочтительно использовать
              канонический `polygon_bind()` (v2).
            • Позволяет привязать сразу несколько полигонов и указывает координаты
              склада явно (`warehouse_location`).
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonAPI_BindPolygon

        Args:
            request: Параметры привязки полигонов по схеме `PolygonBindV1Request`

        Returns:
            Пустой ответ по схеме `PolygonBindV1Response`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.polygon_bind_v1(
                    PolygonBindV1Request(
                        delivery_method_id=123,
                        polygons=[PolygonBindV1Polygon(polygon_id=456, time=30)],
                        warehouse_location=PolygonBindV1WarehouseLocation(
                            lat="58.27", lon="92.13"
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="polygon/bind",
            payload=request.model_dump(),
        )
        return PolygonBindV1Response(**response)
