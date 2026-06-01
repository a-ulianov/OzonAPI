from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsUpdateVoucherRequest,
    SellerActionsUpdateVoucherResponse,
)


class SellerActionsUpdateVoucherMixin(APIManager):
    """Реализует метод /v1/seller-actions/update/voucher"""

    async def seller_actions_update_voucher(
            self: "SellerActionsUpdateVoucherMixin",
            request: SellerActionsUpdateVoucherRequest,
    ) -> SellerActionsUpdateVoucherResponse:
        """Обновляет акцию продавца с механикой «Скидка по промокоду».

        Notes:
            • Новые параметры передаются в объекте `action_parameters`.
            • Даты передаются строкой в формате RFC3339.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateVoucher

        Args:
            request: Идентификатор акции и новые параметры по схеме
                `SellerActionsUpdateVoucherRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsUpdateVoucherResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_update_voucher(
                    SellerActionsUpdateVoucherRequest(
                        action_id=123456,
                        action_parameters=SellerActionsUpdateVoucherParameters(
                            title="Промокод на лето",
                            date_start="2026-07-01T00:00:00Z",
                            date_end="2026-08-15T23:59:59Z",
                            discount_value=15.0,
                            budget=100000,
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/voucher",
            payload=request.model_dump(),
        )
        return SellerActionsUpdateVoucherResponse(**response)
