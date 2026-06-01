from ...core import APIManager
from ...schemas.warehouses import (
    DeliveryMethodReturnSettingsRequest,
    DeliveryMethodReturnSettingsResponse,
)


class DeliveryMethodReturnSettingsGetMixin(APIManager):
    """Реализует метод /v1/delivery-method/return/settings/get"""

    async def delivery_method_return_settings_get(
            self: "DeliveryMethodReturnSettingsGetMixin",
            request: DeliveryMethodReturnSettingsRequest
    ) -> DeliveryMethodReturnSettingsResponse:
        """Возвращает возвратные настройки метода доставки rFBS и rFBS Express.

        Notes:
            • Возвращает настройки возврата курьером, в отделение и транспортной
              компанией для указанного метода доставки.

        References:
            https://docs.ozon.ru/api/seller/#operation/GetDeliveryMethodReturnSettingsV1

        Args:
            request: Запрос по схеме `DeliveryMethodReturnSettingsRequest`

        Returns:
            Возвратные настройки по схеме `DeliveryMethodReturnSettingsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.delivery_method_return_settings_get(
                    DeliveryMethodReturnSettingsRequest(delivery_method_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="delivery-method/return/settings/get",
            payload=request.model_dump(by_alias=True)
        )
        return DeliveryMethodReturnSettingsResponse(**response)
