from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsUpdateMultiLevelDiscountRequest,
    SellerActionsUpdateMultiLevelDiscountResponse,
)


class SellerActionsUpdateMultiLevelDiscountMixin(APIManager):
    """Реализует метод /v1/seller-actions/update/multi-level-discount"""

    async def seller_actions_update_multi_level_discount(
            self: "SellerActionsUpdateMultiLevelDiscountMixin",
            request: SellerActionsUpdateMultiLevelDiscountRequest,
    ) -> SellerActionsUpdateMultiLevelDiscountResponse:
        """Обновляет акцию продавца с механикой «Многоуровневая скидка от суммы».

        Notes:
            • Новые параметры передаются в объекте `action_parameters`.
            • Уровни скидки задаются списком `discount_levels`.
            • Даты передаются строкой в формате RFC3339.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateMultiLevelDiscount

        Args:
            request: Идентификатор акции и новые параметры по схеме
                `SellerActionsUpdateMultiLevelDiscountRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsUpdateMultiLevelDiscountResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_update_multi_level_discount(
                    SellerActionsUpdateMultiLevelDiscountRequest(
                        action_id=123456,
                        action_parameters=SellerActionsUpdateMultiLevelDiscountParameters(
                            title="Чем больше, тем дешевле",
                            date_start="2026-07-01T00:00:00Z",
                            date_end="2026-08-15T23:59:59Z",
                            is_legal_entities_segment=False,
                            discount_levels=[
                                SellerActionDiscountLevel(order_amount=3000.0, discount_value=5.0),
                            ],
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/multi-level-discount",
            payload=request.model_dump(),
        )
        return SellerActionsUpdateMultiLevelDiscountResponse(**response)
