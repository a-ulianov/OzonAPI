from ...core import APIManager
from ...schemas.returns import (
    ReturnsSettingsUtilizationUpdateRequest,
    ReturnsSettingsUtilizationUpdateResponse,
)


class ReturnsSettingsUtilizationUpdateMixin(APIManager):
    """Реализует метод /v1/returns/settings/utilization/update"""

    async def returns_settings_utilization_update(
            self: "ReturnsSettingsUtilizationUpdateMixin",
            request: ReturnsSettingsUtilizationUpdateRequest
    ) -> ReturnsSettingsUtilizationUpdateResponse:
        """Метод для обновления настроек автоутилизации.

        Notes:
            • Включает/выключает автоутилизацию и задаёт стоимость для товаров без брака и с браком.
            • При успешном обновлении возвращается пустой ответ.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsSettingsUtilizationUpdate

        Args:
            request: Запрос на обновление настроек по схеме `ReturnsSettingsUtilizationUpdateRequest`

        Returns:
            Результат обновления по схеме `ReturnsSettingsUtilizationUpdateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_settings_utilization_update(
                    ReturnsSettingsUtilizationUpdateRequest(
                        utilization_price=ReturnsSettingsUtilizationUpdatePrice(enabled=True, value=100),
                        utilization_price_defects=ReturnsSettingsUtilizationUpdatePrice(enabled=False)
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="returns/settings/utilization/update",
            payload=request.model_dump()
        )
        return ReturnsSettingsUtilizationUpdateResponse(**response)
