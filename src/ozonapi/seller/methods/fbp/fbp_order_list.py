from ...core import APIManager
from ...schemas.fbp import FbpOrderListRequest, FbpOrderListResponse


class FbpOrderListMixin(APIManager):
    """Реализует метод /v1/fbp/order/list"""

    async def fbp_order_list(
            self: "FbpOrderListMixin",
            request: FbpOrderListRequest,
    ) -> FbpOrderListResponse:
        """Получает список поставок.

        Notes:
            • Поддерживает постраничную выборку по `last_id`.
            • Признак `has_next` указывает на наличие следующей страницы.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderList

        Args:
            request: Параметры выборки по схеме `FbpOrderListRequest`

        Returns:
            Список поставок по схеме `FbpOrderListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_list(
                    FbpOrderListRequest(count=50)
                )

            for item in result.items:
                print(item.id, item.supply_id, item.status)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/list",
            payload=request.model_dump(),
        )
        return FbpOrderListResponse(**response)
