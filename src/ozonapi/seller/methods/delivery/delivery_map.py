from ...core import APIManager
from ...schemas.delivery import DeliveryMapRequest, DeliveryMapResponse


class DeliveryMapMixin(APIManager):
    """Реализует метод /v1/delivery/map"""

    async def delivery_map(
            self: "DeliveryMapMixin",
            request: DeliveryMapRequest
    ) -> DeliveryMapResponse:
        """Возвращает список точек самовывоза на карте в указанной области.

        Notes:
            • Точки группируются в кластеры в зависимости от масштаба `zoom`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DeliveryMap

        Args:
            request: Запрос по схеме `DeliveryMapRequest`

        Returns:
            Кластеры точек самовывоза по схеме `DeliveryMapResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_map(
                    DeliveryMapRequest(
                        viewport={
                            "left_bottom": {"lat": 55.7, "long": 37.5},
                            "right_top": {"lat": 55.8, "long": 37.7},
                        },
                        zoom=12,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery/map",
            payload=request.model_dump()
        )
        return DeliveryMapResponse(**response)
