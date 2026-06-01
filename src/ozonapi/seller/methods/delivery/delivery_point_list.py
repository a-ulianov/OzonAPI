from ...core import APIManager
from ...schemas.delivery import (
    DeliveryPointListRequest,
    DeliveryPointListResponse,
)


class DeliveryPointListMixin(APIManager):
    """Реализует метод /v1/delivery/point/list"""

    async def delivery_point_list(
            self: "DeliveryPointListMixin",
            request: DeliveryPointListRequest
    ) -> DeliveryPointListResponse:
        """Возвращает список всех точек самовывоза.

        Notes:
            • Подробную информацию о точке получите методом `delivery_point_info()`
              по `map_point_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DeliveryAPI_DeliveryPointList

        Args:
            request: Запрос по схеме `DeliveryPointListRequest`

        Returns:
            Список точек самовывоза по схеме `DeliveryPointListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_point_list(DeliveryPointListRequest())
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery/point/list",
            payload=request.model_dump()
        )
        return DeliveryPointListResponse(**response)
