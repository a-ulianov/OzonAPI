from ...core import APIManager
from ...schemas.polygons import PolygonListRequest, PolygonListResponse


class PolygonListMixin(APIManager):
    """Реализует метод /v1/polygon/list"""

    async def polygon_list(
            self: "PolygonListMixin",
            request: PolygonListRequest,
    ) -> PolygonListResponse:
        """Получает список установленных полигонов на метод доставки.

        Notes:
            • Возвращает полигоны, привязанные к указанному методу доставки на складе,
              вместе с их координатами и временем доставки.

        References:
            https://docs.ozon.ru/api/seller/?#operation/PolygonList

        Args:
            request: Идентификаторы метода доставки и склада по схеме `PolygonListRequest`

        Returns:
            Список полигонов по схеме `PolygonListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.polygon_list(
                    PolygonListRequest(delivery_method_id=123, warehouse_id=789)
                )

            for polygon in result.polygons:
                print(polygon.polygon_id, polygon.time)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="polygon/list",
            payload=request.model_dump(),
        )
        return PolygonListResponse(**response)
