from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsCreateDiscountRequest,
    SellerActionsCreateDiscountResponse,
)


class SellerActionsCreateDiscountMixin(APIManager):
    """Реализует метод /v1/seller-actions/create/discount"""

    async def seller_actions_create_discount(
            self: "SellerActionsCreateDiscountMixin",
            request: SellerActionsCreateDiscountRequest,
    ) -> SellerActionsCreateDiscountResponse:
        """Создаёт акцию продавца с механикой «Скидка».

        Notes:
            • Акция применяет указанную минимальную скидку к добавленным товарам.
            • Даты `date_start` и `date_end` передаются строкой в формате RFC3339.
            • После создания добавьте товары методом `seller_actions_products_add()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateDiscount

        Args:
            request: Параметры новой акции по схеме `SellerActionsCreateDiscountRequest`

        Returns:
            Идентификатор созданной акции по схеме `SellerActionsCreateDiscountResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_create_discount(
                    SellerActionsCreateDiscountRequest(
                        title="Летняя распродажа",
                        date_start="2026-07-01T00:00:00Z",
                        date_end="2026-07-31T23:59:59Z",
                        min_action_percent=10.0,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/discount",
            payload=request.model_dump(),
        )
        return SellerActionsCreateDiscountResponse(**response)
