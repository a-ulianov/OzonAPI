from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsUpdateDiscountRequest,
    SellerActionsUpdateDiscountResponse,
)


class SellerActionsUpdateDiscountMixin(APIManager):
    """Реализует метод /v1/seller-actions/update/discount"""

    async def seller_actions_update_discount(
            self: "SellerActionsUpdateDiscountMixin",
            request: SellerActionsUpdateDiscountRequest,
    ) -> SellerActionsUpdateDiscountResponse:
        """Обновляет акцию продавца с механикой «Скидка».

        Notes:
            • Новые параметры передаются в объекте `action_parameters`.
            • Даты передаются строкой в формате RFC3339.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateDiscount

        Args:
            request: Идентификатор акции и новые параметры по схеме
                `SellerActionsUpdateDiscountRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsUpdateDiscountResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_update_discount(
                    SellerActionsUpdateDiscountRequest(
                        action_id=123456,
                        action_parameters=SellerActionsUpdateDiscountParameters(
                            title="Летняя распродажа",
                            date_start="2026-07-01T00:00:00Z",
                            date_end="2026-08-15T23:59:59Z",
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/discount",
            payload=request.model_dump(),
        )
        return SellerActionsUpdateDiscountResponse(**response)
