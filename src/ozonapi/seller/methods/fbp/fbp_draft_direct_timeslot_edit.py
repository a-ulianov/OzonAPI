from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectTimeslotEditRequest,
    FbpDraftDirectTimeslotEditResponse,
)


class FbpDraftDirectTimeslotEditMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/timeslot/edit"""

    async def fbp_draft_direct_timeslot_edit(
            self: "FbpDraftDirectTimeslotEditMixin",
            request: FbpDraftDirectTimeslotEditRequest,
    ) -> FbpDraftDirectTimeslotEditResponse:
        """Редактирует таймслот в черновике.

        Notes:
            • При ошибке брони таймслота заполняется `error_reasons`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectTimeslotEdit

        Args:
            request: Параметры изменения таймслота по схеме
                `FbpDraftDirectTimeslotEditRequest`

        Returns:
            Результат изменения по схеме `FbpDraftDirectTimeslotEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_timeslot_edit(
                    FbpDraftDirectTimeslotEditRequest(
                        supply_id="123",
                        row_version=1,
                        timeslot_start="2026-06-11T10:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/timeslot/edit",
            payload=request.model_dump(),
        )
        return FbpDraftDirectTimeslotEditResponse(**response)
