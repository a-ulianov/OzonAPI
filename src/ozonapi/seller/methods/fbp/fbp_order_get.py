from ...core import APIManager
from ...schemas.fbp import FbpOrderGetRequest, FbpOrderGetResponse


class FbpOrderGetMixin(APIManager):
    """Реализует метод /v1/fbp/order/get"""

    async def fbp_order_get(
            self: "FbpOrderGetMixin",
            request: FbpOrderGetRequest,
    ) -> FbpOrderGetResponse:
        """Получает информацию о конкретной поставке.

        Notes:
            • Возвращает статус поставки, детали доставки, состояние отмены и
              признаки доступных действий.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderGet

        Args:
            request: Идентификатор поставки по схеме `FbpOrderGetRequest`

        Returns:
            Информация о поставке по схеме `FbpOrderGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_get(
                    FbpOrderGetRequest(supply_id="70")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/get",
            payload=request.model_dump(),
        )
        return FbpOrderGetResponse(**response)
