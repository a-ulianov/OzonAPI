from ...core import APIManager
from ...schemas.returns import ReturnsSettingsUtilizationInfoResponse


class ReturnsSettingsUtilizationInfoMixin(APIManager):
    """Реализует метод /v1/returns/settings/utilization/info"""

    async def returns_settings_utilization_info(
            self: "ReturnsSettingsUtilizationInfoMixin"
    ) -> ReturnsSettingsUtilizationInfoResponse:
        """Метод для получения настроек автоутилизации.

        Notes:
            • Возвращает текущие настройки автоутилизации возвратов и минимальную стоимость.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsSettingsUtilizationInfo

        Returns:
            Настройки автоутилизации по схеме `ReturnsSettingsUtilizationInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_settings_utilization_info()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="returns/settings/utilization/info",
            payload={}
        )
        return ReturnsSettingsUtilizationInfoResponse(**response)
