from ...core import APIManager
from ...schemas.seller_actions import (
    SellerActionsUpdateInstallmentRequest,
    SellerActionsUpdateInstallmentResponse,
)


class SellerActionsUpdateInstallmentMixin(APIManager):
    """Реализует метод /v1/seller-actions/update/installment"""

    async def seller_actions_update_installment(
            self: "SellerActionsUpdateInstallmentMixin",
            request: SellerActionsUpdateInstallmentRequest,
    ) -> SellerActionsUpdateInstallmentResponse:
        """Обновляет акцию продавца с механикой «Беспроцентная рассрочка».

        Notes:
            • Новые параметры передаются в объекте `action_parameters`.
            • Дата `date_start` передаётся строкой в формате RFC3339.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/SellerActionsUpdateInstallment

        Args:
            request: Идентификатор акции и новые параметры по схеме
                `SellerActionsUpdateInstallmentRequest`

        Returns:
            Пустой ответ по схеме `SellerActionsUpdateInstallmentResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.seller_actions_update_installment(
                    SellerActionsUpdateInstallmentRequest(
                        action_id=123456,
                        action_parameters=SellerActionsUpdateInstallmentParameters(
                            title="Рассрочка на технику",
                            date_start="2026-07-01T00:00:00Z",
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="seller-actions/update/installment",
            payload=request.model_dump(),
        )
        return SellerActionsUpdateInstallmentResponse(**response)
