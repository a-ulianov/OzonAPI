from ...core import APIManager
from ...schemas.delivery import DeliveryCheckRequest, DeliveryCheckResponse


class DeliveryCheckMixin(APIManager):
    """Реализует метод /v1/delivery/check"""

    async def delivery_check(
            self: "DeliveryCheckMixin",
            request: DeliveryCheckRequest
    ) -> DeliveryCheckResponse:
        """Проверяет доступность доставки Ozon для покупателя.

        References:
            https://docs.ozon.ru/api/seller/#operation/DeliveryCheck

        Args:
            request: Запрос по схеме `DeliveryCheckRequest`

        Returns:
            Признак доступности доставки по схеме `DeliveryCheckResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_check(
                    DeliveryCheckRequest(client_phone="+70000000000")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery/check",
            payload=request.model_dump()
        )
        return DeliveryCheckResponse(**response)
