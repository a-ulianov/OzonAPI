from ...core import APIManager
from ...schemas.returns import ReturnsSettingsUtilizationHistoryResponse


class ReturnsSettingsUtilizationHistoryMixin(APIManager):
    """Реализует метод /v1/returns/settings/utilization/history"""

    async def returns_settings_utilization_history(
            self: "ReturnsSettingsUtilizationHistoryMixin"
    ) -> ReturnsSettingsUtilizationHistoryResponse:
        """Метод для получения истории изменений настроек автоутилизации.

        Notes:
            • Возвращает список событий изменения настроек автоутилизации возвратов.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ReturnsAPI_ReturnsSettingsUtilizationHistory

        Returns:
            История изменений по схеме `ReturnsSettingsUtilizationHistoryResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.returns_settings_utilization_history()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="returns/settings/utilization/history",
            payload={}
        )
        return ReturnsSettingsUtilizationHistoryResponse(**response)
