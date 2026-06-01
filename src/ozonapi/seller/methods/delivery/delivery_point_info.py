from ...core import APIManager
from ...schemas.delivery import (
    DeliveryPointInfoRequest,
    DeliveryPointInfoResponse,
)


class DeliveryPointInfoMixin(APIManager):
    """Реализует метод /v1/delivery/point/info"""

    async def delivery_point_info(
            self: "DeliveryPointInfoMixin",
            request: DeliveryPointInfoRequest
    ) -> DeliveryPointInfoResponse:
        """Возвращает подробную информацию о выбранных точках самовывоза.

        Notes:
            • `map_point_ids` получите методами `delivery_map()` или
              `delivery_point_list()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DeliveryPointInfo

        Args:
            request: Запрос по схеме `DeliveryPointInfoRequest`

        Returns:
            Информация о точках по схеме `DeliveryPointInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_point_info(
                    DeliveryPointInfoRequest(map_point_ids=["123"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery/point/info",
            payload=request.model_dump()
        )
        return DeliveryPointInfoResponse(**response)
