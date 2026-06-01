from ...core import APIManager
from ...schemas.polygons import PolygonDeleteRequest, PolygonDeleteResponse


class PolygonDeleteMixin(APIManager):
    """Реализует метод /v1/polygon/delete"""

    async def polygon_delete(
            self: "PolygonDeleteMixin",
            request: PolygonDeleteRequest,
    ) -> PolygonDeleteResponse:
        """Удаляет полигон из области доставки.

        Notes:
            • Удаляет связь полигона с методом доставки на указанном складе.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonDelete

        Args:
            request: Параметры удаления полигона по схеме `PolygonDeleteRequest`

        Returns:
            Пустой ответ по схеме `PolygonDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.polygon_delete(
                    PolygonDeleteRequest(
                        delivery_method_id=123, polygon_id=456, warehouse_id=789
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="polygon/delete",
            payload=request.model_dump(),
        )
        return PolygonDeleteResponse(**response)
