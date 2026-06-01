from ...core import APIManager
from ...schemas.polygons import (
    PolygonTimeCoordinatesUpdateRequest,
    PolygonTimeCoordinatesUpdateResponse,
)


class PolygonTimeCoordinatesUpdateMixin(APIManager):
    """Реализует метод /v1/polygon/time/coordinates/update"""

    async def polygon_time_coordinates_update(
            self: "PolygonTimeCoordinatesUpdateMixin",
            request: PolygonTimeCoordinatesUpdateRequest,
    ) -> PolygonTimeCoordinatesUpdateResponse:
        """Обновляет координаты полигона доставки.

        Notes:
            • Изменяет координаты ранее созданного полигона.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonTimeCoordinatesUpdate

        Args:
            request: Новые координаты полигона по схеме
                `PolygonTimeCoordinatesUpdateRequest`

        Returns:
            Пустой ответ по схеме `PolygonTimeCoordinatesUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.polygon_time_coordinates_update(
                    PolygonTimeCoordinatesUpdateRequest(
                        coordinates="[[[58.27,92.13],[58.30,92.16],[58.27,92.13]]]",
                        delivery_method_id=123,
                        polygon_id=456,
                        warehouse_id=789,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="polygon/time/coordinates/update",
            payload=request.model_dump(),
        )
        return PolygonTimeCoordinatesUpdateResponse(**response)
