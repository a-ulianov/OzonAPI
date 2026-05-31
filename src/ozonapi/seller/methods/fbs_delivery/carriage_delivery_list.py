from ...core import APIManager
from ...schemas.fbs_delivery import (
    CarriageDeliveryListRequest,
    CarriageDeliveryListResponse,
)


class CarriageDeliveryListMixin(APIManager):
    """Реализует метод /v2/carriage/delivery/list"""

    async def carriage_delivery_list(
            self: "CarriageDeliveryListMixin",
            request: CarriageDeliveryListRequest
    ) -> CarriageDeliveryListResponse:
        """Метод для получения списка методов доставки и отгрузок (v2).

        Notes:
            • Использует курсорную пагинацию: передайте `cursor` из предыдущего ответа,
              пока `has_next` равно `true`.
            • Фильтруйте по методу доставки и дате отгрузки через объект `filter`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageDeliveryListV2

        Args:
            request: Запрос на получение списка методов доставки по схеме `CarriageDeliveryListRequest`

        Returns:
            Список методов доставки и отгрузок по схеме `CarriageDeliveryListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_delivery_list(
                    CarriageDeliveryListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="carriage/delivery/list",
            payload=request.model_dump()
        )
        return CarriageDeliveryListResponse(**response)
