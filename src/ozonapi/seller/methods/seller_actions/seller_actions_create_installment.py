from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsCreateInstallmentRequest,
    SellerActionsCreateInstallmentResponse,
)


class SellerActionsCreateInstallmentMixin(APIManager):
    """Реализует метод /v1/seller-actions/create/installment"""

    async def seller_actions_create_installment(
            self: "SellerActionsCreateInstallmentMixin",
            request: SellerActionsCreateInstallmentRequest,
    ) -> SellerActionsCreateInstallmentResponse:
        """Создаёт акцию продавца с механикой «Беспроцентная рассрочка».

        Notes:
            • Дата `date_start` передаётся строкой в формате RFC3339.
            • После создания добавьте товары методом `seller_actions_products_add()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsCreateInstallment

        Args:
            request: Параметры новой акции по схеме `SellerActionsCreateInstallmentRequest`

        Returns:
            Идентификатор созданной акции по схеме `SellerActionsCreateInstallmentResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.seller_actions_create_installment(
                    SellerActionsCreateInstallmentRequest(
                        title="Рассрочка на технику",
                        date_start="2026-07-01T00:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/create/installment",
            payload=request.model_dump(),
        )
        return SellerActionsCreateInstallmentResponse(**response)
