from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectSellerDlvEditRequest,
    FbpDraftDirectSellerDlvEditResponse,
)


class FbpDraftDirectSellerDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/seller-dlv/edit"""

    async def fbp_draft_direct_seller_dlv_edit(
            self: "FbpDraftDirectSellerDlvEditMixin",
            request: FbpDraftDirectSellerDlvEditRequest,
    ) -> FbpDraftDirectSellerDlvEditResponse:
        """Обновляет информацию о доставке силами продавца в черновике.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.
            • При ошибке валидации `is_error=true` и заполняется `error.errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectSellerDlvEdit

        Args:
            request: Параметры обновления по схеме `FbpDraftDirectSellerDlvEditRequest`

        Returns:
            Результат обновления по схеме `FbpDraftDirectSellerDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_seller_dlv_edit(
                    FbpDraftDirectSellerDlvEditRequest(
                        supply_id="123",
                        row_version=1,
                        driver_name="Иванов И.И.",
                        vehicle_number="А123ВС777",
                        vehicle_type="Грузовой",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/seller-dlv/edit",
            payload=request.model_dump(),
        )
        return FbpDraftDirectSellerDlvEditResponse(**response)
