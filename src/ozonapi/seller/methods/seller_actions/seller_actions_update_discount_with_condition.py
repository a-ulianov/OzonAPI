from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsUpdateDiscountWithConditionRequest,
    SellerActionsUpdateDiscountWithConditionResponse,
)


class SellerActionsUpdateDiscountWithConditionMixin(APIManager):
    """Реализует метод /v1/seller-actions/update/discount-with-condition"""

    async def seller_actions_update_discount_with_condition(
            self: "SellerActionsUpdateDiscountWithConditionMixin",
            request: SellerActionsUpdateDiscountWithConditionRequest,
    ) -> SellerActionsUpdateDiscountWithConditionResponse:
        """Обновляет акцию продавца с механикой «Скидка от суммы заказа».

        Notes:
            • Новые параметры передаются в объекте `action_parameters`.
            • Даты передаются строкой в формате RFC3339.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateDiscountWithCondition

        Args:
            request: Идентификатор акции и новые параметры по схеме
                `SellerActionsUpdateDiscountWithConditionRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsUpdateDiscountWithConditionResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_update_discount_with_condition(
                    SellerActionsUpdateDiscountWithConditionRequest(
                        action_id=123456,
                        action_parameters=SellerActionsUpdateDiscountWithConditionParameters(
                            title="Скидка от 5000",
                            date_start="2026-07-01T00:00:00Z",
                            date_end="2026-08-15T23:59:59Z",
                            discount_value=20.0,
                            min_order_amount=5000.0,
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/discount-with-condition",
            payload=request.model_dump(),
        )
        return SellerActionsUpdateDiscountWithConditionResponse(**response)
