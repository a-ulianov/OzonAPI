from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsCreateVoucherRequest,
    SellerActionsCreateVoucherResponse,
)


class SellerActionsCreateVoucherMixin(APIManager):
    """Реализует метод /v1/seller-actions/create/voucher"""

    async def seller_actions_create_voucher(
            self: "SellerActionsCreateVoucherMixin",
            request: SellerActionsCreateVoucherRequest,
    ) -> SellerActionsCreateVoucherResponse:
        """Создаёт акцию продавца с механикой «Скидка по промокоду».

        Notes:
            • Параметры промокода задаются объектом `voucher_parameters`.
            • При исчерпании бюджета (`budget`) акция автоматически останавливается.
            • Список промокодов выгружается методом `seller_actions_voucher_get()`.
            • Даты передаются строкой в формате RFC3339.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateVoucher

        Args:
            request: Параметры новой акции по схеме `SellerActionsCreateVoucherRequest`

        Returns:
            Идентификатор созданной акции по схеме `SellerActionsCreateVoucherResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_create_voucher(
                    SellerActionsCreateVoucherRequest(
                        title="Промокод на лето",
                        date_start="2026-07-01T00:00:00Z",
                        date_end="2026-07-31T23:59:59Z",
                        discount_type="PERCENT",
                        discount_value=10.0,
                        voucher_parameters=SellerActionsCreateVoucherParameter(
                            type="UNIQUE", count_codes=100, is_private=True
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/voucher",
            payload=request.model_dump(),
        )
        return SellerActionsCreateVoucherResponse(**response)
