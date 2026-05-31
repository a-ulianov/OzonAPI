from ...core import APIManager
from ...schemas.fbs_delivery import (
    CarriageDeliveryListV1Request,
    CarriageDeliveryListV1Response,
)


class CarriageDeliveryListV1Mixin(APIManager):
    """Реализует метод /v1/carriage/delivery/list"""

    async def carriage_delivery_list_v1(
            self: "CarriageDeliveryListV1Mixin",
            request: CarriageDeliveryListV1Request
    ) -> CarriageDeliveryListV1Response:
        """Метод для получения списка методов доставки и отгрузок (v1).

        Notes:
            • Устаревшая версия метода без пагинации; для новых интеграций используйте
              `carriage_delivery_list()` (v2).
            • Фильтрует по методу доставки и дате отгрузки.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageDeliveryList

        Args:
            request: Запрос на получение списка методов доставки по схеме `CarriageDeliveryListV1Request`

        Returns:
            Список методов доставки и отгрузок по схеме `CarriageDeliveryListV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_delivery_list_v1(
                    CarriageDeliveryListV1Request(
                        delivery_method_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/delivery/list",
            payload=request.model_dump()
        )
        return CarriageDeliveryListV1Response(**response)
