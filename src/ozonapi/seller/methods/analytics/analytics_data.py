from ...core import APIManager
from ...schemas.analytics import (
    AnalyticsDataRequest,
    AnalyticsDataResponse,
)


class AnalyticsDataMixin(APIManager):
    """Реализует метод /v1/analytics/data"""

    async def analytics_data(
            self: "AnalyticsDataMixin",
            request: AnalyticsDataRequest,
    ) -> AnalyticsDataResponse:
        """Получает данные аналитики по товарам (Premium).

        Notes:
            • Метод доступен продавцам с подпиской Premium Plus.
            • Данные группируются по измерениям `dimension` и считаются по `metrics`.
            • Даты `date_from`/`date_to` передаются строками в формате YYYY-MM-DD.
            • В ответе `result.data[].metrics` — массив значений в порядке `metrics`.

        References:
            https://docs.ozon.ru/api/seller/#operation/AnalyticsAPI_AnalyticsGetData

        Args:
            request: Параметры аналитического запроса по схеме `AnalyticsDataRequest`

        Returns:
            Данные аналитики по схеме `AnalyticsDataResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.analytics_data(
                    AnalyticsDataRequest(
                        date_from="2026-05-01",
                        date_to="2026-05-31",
                        dimension=["sku"],
                        metrics=["revenue", "ordered_units"],
                        limit=100,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="analytics/data",
            payload=request.model_dump(),
        )
        return AnalyticsDataResponse(**response)
