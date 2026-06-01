from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsCreateDiscountWithConditionRequest,
    SellerActionsCreateDiscountWithConditionResponse,
)


class SellerActionsCreateDiscountWithConditionMixin(APIManager):
    """Реализует метод /v1/seller-actions/create/discount-with-condition"""

    async def seller_actions_create_discount_with_condition(
            self: "SellerActionsCreateDiscountWithConditionMixin",
            request: SellerActionsCreateDiscountWithConditionRequest,
    ) -> SellerActionsCreateDiscountWithConditionResponse:
        """Создаёт акцию продавца с механикой «Скидка от суммы заказа».

        Notes:
            • Скидка применяется, когда сумма заказа достигает `min_order_amount`.
            • Тип скидки задаётся полем `discount_type` (`PERCENT` или `CURRENCY`).
            • Даты передаются строкой в формате RFC3339.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateDiscountWithCondition

        Args:
            request: Параметры новой акции по схеме
                `SellerActionsCreateDiscountWithConditionRequest`

        Returns:
            Идентификатор созданной акции по схеме
            `SellerActionsCreateDiscountWithConditionResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_create_discount_with_condition(
                    SellerActionsCreateDiscountWithConditionRequest(
                        title="Скидка от 5000",
                        date_start="2026-07-01T00:00:00Z",
                        date_end="2026-07-31T23:59:59Z",
                        discount_type="PERCENT",
                        discount_value=15.0,
                        min_order_amount=5000.0,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/discount-with-condition",
            payload=request.model_dump(),
        )
        return SellerActionsCreateDiscountWithConditionResponse(**response)
