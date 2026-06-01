from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectTplDlvEditRequest,
    FbpDraftDirectTplDlvEditResponse,
)


class FbpDraftDirectTplDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/tpl-dlv/edit"""

    async def fbp_draft_direct_tpl_dlv_edit(
            self: "FbpDraftDirectTplDlvEditMixin",
            request: FbpDraftDirectTplDlvEditRequest,
    ) -> FbpDraftDirectTplDlvEditResponse:
        """Редактирует черновик поставки со способом доставки сторонней ТК.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.
            • При ошибке валидации `is_error=true` и заполняется `error.errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectTplDlvEdit

        Args:
            request: Параметры редактирования по схеме `FbpDraftDirectTplDlvEditRequest`

        Returns:
            Результат редактирования по схеме `FbpDraftDirectTplDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_tpl_dlv_edit(
                    FbpDraftDirectTplDlvEditRequest(
                        supply_id="123",
                        row_version=1,
                        tracking_number="TRK-123",
                        transport_company_name="СДЭК",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/tpl-dlv/edit",
            payload=request.model_dump(),
        )
        return FbpDraftDirectTplDlvEditResponse(**response)
