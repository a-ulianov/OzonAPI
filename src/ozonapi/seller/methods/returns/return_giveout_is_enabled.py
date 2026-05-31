from ...core import APIManager
from ...schemas.returns import ReturnGiveoutIsEnabledResponse


class ReturnGiveoutIsEnabledMixin(APIManager):
    """Реализует метод /v1/return/giveout/is-enabled"""

    async def return_giveout_is_enabled(
            self: "ReturnGiveoutIsEnabledMixin"
    ) -> ReturnGiveoutIsEnabledResponse:
        """Метод для проверки возможности получения возвратных отгрузок по штрихкоду.

        Notes:
            • Возвращает признак доступности получения возвратных отгрузок по штрихкоду.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutIsEnabled

        Returns:
            Признак доступности по схеме `ReturnGiveoutIsEnabledResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_is_enabled()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/is-enabled",
            payload={}
        )
        return ReturnGiveoutIsEnabledResponse(**response)
