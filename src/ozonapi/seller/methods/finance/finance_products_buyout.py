from ...core import APIManager
from ...schemas.finance import (
    FinanceProductsBuyoutRequest,
    FinanceProductsBuyoutResponse,
)


class FinanceProductsBuyoutMixin(APIManager):
    """Реализует метод /v1/finance/products/buyout"""

    async def finance_products_buyout(
            self: "FinanceProductsBuyoutMixin",
            request: FinanceProductsBuyoutRequest
    ) -> FinanceProductsBuyoutResponse:
        """Возвращает отчёт о выкупленных товарах за период.

        Notes:
            • Содержит цену выкупа, сумму к начислению, ставку НДС и скидку по категории
              по каждому выкупленному товару.

        References:
            https://docs.ozon.ru/api/seller/#operation/FinanceAPI_GetFinanceProductsBuyout

        Args:
            request: Запрос отчёта по схеме `FinanceProductsBuyoutRequest`

        Returns:
            Отчёт о выкупах по схеме `FinanceProductsBuyoutResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.finance_products_buyout(
                    FinanceProductsBuyoutRequest(
                        date_from="2026-04-01", date_to="2026-04-30"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="finance/products/buyout",
            payload=request.model_dump(by_alias=True)
        )
        return FinanceProductsBuyoutResponse(**response)
