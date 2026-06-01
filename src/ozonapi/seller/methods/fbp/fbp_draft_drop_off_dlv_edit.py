from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffDlvEditRequest,
    FbpDraftDropOffDlvEditResponse,
)


class FbpDraftDropOffDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/dlv/edit"""

    async def fbp_draft_drop_off_dlv_edit(
            self: "FbpDraftDropOffDlvEditMixin",
            request: FbpDraftDropOffDlvEditRequest,
    ) -> FbpDraftDropOffDlvEditResponse:
        """Редактирует детали доставки для drop-off черновика.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffDlvEdit

        Args:
            request: Параметры редактирования по схеме `FbpDraftDropOffDlvEditRequest`

        Returns:
            Обновлённая версия записи по схеме `FbpDraftDropOffDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_dlv_edit(
                    FbpDraftDropOffDlvEditRequest(
                        supply_id="55",
                        row_version=1,
                        drop_off_date="2026-06-11T10:00:00Z",
                        drop_off_point_id=7,
                        drop_off_province_uuid="uuid-1",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/dlv/edit",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffDlvEditResponse(**response)
