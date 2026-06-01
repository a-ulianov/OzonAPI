from ...core import APIManager
from ...schemas.beta import SellerOzonLogisticsInfoResponse


class SellerOzonLogisticsInfoMixin(APIManager):
    """Реализует метод /v1/seller/ozon-logistics/info"""

    async def seller_ozon_logistics_info(
            self: "SellerOzonLogisticsInfoMixin",
    ) -> SellerOzonLogisticsInfoResponse:
        """Метод для получения информации о подключении продавца к Ozon Логистике.

        Notes:
            • Метод не требует передачи параметров в теле запроса.
            • Возвращает признак подключения к Ozon Логистике и список доступных схем работы.
            • Известные значения схем: `UNKNOWN`, `FBO`, `FBS` (набор может расширяться).

        References:
            https://docs.ozon.ru/api/seller/?#operation/SellerAPI_SellerOzonLogisticsInfo

        Returns:
            Ответ с информацией о подключении к Ozon Логистике по схеме
            `SellerOzonLogisticsInfoResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_ozon_logistics_info()

            enabled = result.ozon_logistics_enabled
            schemas = result.available_schemas
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller/ozon-logistics/info",
            payload={},
        )
        return SellerOzonLogisticsInfoResponse(**response)
