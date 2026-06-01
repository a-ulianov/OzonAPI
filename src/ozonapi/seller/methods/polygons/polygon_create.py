from ...core import APIManager
from ...schemas.polygons import PolygonCreateRequest, PolygonCreateResponse


class PolygonCreateMixin(APIManager):
    """Реализует метод /v1/polygon/create"""

    async def polygon_create(
            self: "PolygonCreateMixin",
            request: PolygonCreateRequest,
    ) -> PolygonCreateResponse:
        """Создаёт полигон доставки.

        Notes:
            • Координаты полигона задаются строкой с JSON-массивом точек
              `[[[lat, lon], [lat, lon], ...]]`.
            • Координаты можно получить, например, через geojson.io.
            • После создания полигон нужно привязать к методу доставки методом
              `polygon_bind()`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonAPI_CreatePolygon

        Args:
            request: Координаты полигона по схеме `PolygonCreateRequest`

        Returns:
            Идентификатор созданного полигона по схеме `PolygonCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.polygon_create(
                    PolygonCreateRequest(
                        coordinates="[[[58.27,92.13],[58.30,92.16],[58.27,92.13]]]"
                    )
                )

            polygon_id = result.polygon_id
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="polygon/create",
            payload=request.model_dump(),
        )
        return PolygonCreateResponse(**response)
