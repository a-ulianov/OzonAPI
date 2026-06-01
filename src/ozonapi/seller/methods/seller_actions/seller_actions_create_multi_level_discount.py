from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsCreateMultiLevelDiscountRequest,
    SellerActionsCreateMultiLevelDiscountResponse,
)


class SellerActionsCreateMultiLevelDiscountMixin(APIManager):
    """Реализует метод /v1/seller-actions/create/multi-level-discount"""

    async def seller_actions_create_multi_level_discount(
            self: "SellerActionsCreateMultiLevelDiscountMixin",
            request: SellerActionsCreateMultiLevelDiscountRequest,
    ) -> SellerActionsCreateMultiLevelDiscountResponse:
        """Создаёт акцию продавца с механикой «Многоуровневая скидка от суммы».

        Notes:
            • Уровни скидки задаются списком `discount_levels` (сумма заказа → размер скидки).
            • Тип скидки задаётся полем `discount_type` (`PERCENT` или `CURRENCY`).
            • Даты передаются строкой в формате RFC3339.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateMultiLevelDiscount

        Args:
            request: Параметры новой акции по схеме
                `SellerActionsCreateMultiLevelDiscountRequest`

        Returns:
            Идентификатор созданной акции по схеме
            `SellerActionsCreateMultiLevelDiscountResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_create_multi_level_discount(
                    SellerActionsCreateMultiLevelDiscountRequest(
                        title="Чем больше, тем дешевле",
                        date_start="2026-07-01T00:00:00Z",
                        date_end="2026-07-31T23:59:59Z",
                        discount_type="PERCENT",
                        is_legal_entities_segment=False,
                        discount_levels=[
                            SellerActionDiscountLevel(order_amount=3000.0, discount_value=5.0),
                            SellerActionDiscountLevel(order_amount=6000.0, discount_value=10.0),
                        ],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/multi-level-discount",
            payload=request.model_dump(),
        )
        return SellerActionsCreateMultiLevelDiscountResponse(**response)
