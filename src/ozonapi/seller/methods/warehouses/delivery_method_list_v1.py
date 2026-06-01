from ...core import APIManager
from ...schemas.warehouses import (
    DeliveryMethodListV1Request,
    DeliveryMethodListV1Response,
)


class DeliveryMethodListV1Mixin(APIManager):
    """Реализует метод /v1/delivery-method/list"""

    async def delivery_method_list_v1(
            self: "DeliveryMethodListV1Mixin",
            request: DeliveryMethodListV1Request = DeliveryMethodListV1Request()
    ) -> DeliveryMethodListV1Response:
        """Возвращает список методов доставки склада (устаревшая версия 1).

        Notes:
            • Постраничная выдача через `limit`/`offset`.
            • Рекомендуется использовать `delivery_method_list()` (v2).

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseAPI_DeliveryMethodList

        Args:
            request: Параметры запроса по схеме `DeliveryMethodListV1Request`

        Returns:
            Список методов доставки по схеме `DeliveryMethodListV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_method_list_v1()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery-method/list",
            payload=request.model_dump(by_alias=True)
        )
        return DeliveryMethodListV1Response(**response)
