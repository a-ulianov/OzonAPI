from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectTimeslotGetRequest,
    FbpDraftDirectTimeslotGetResponse,
)


class FbpDraftDirectTimeslotGetMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/timeslot/get"""

    async def fbp_draft_direct_timeslot_get(
            self: "FbpDraftDirectTimeslotGetMixin",
            request: FbpDraftDirectTimeslotGetRequest,
    ) -> FbpDraftDirectTimeslotGetResponse:
        """Получает список таймслотов для прямой поставки.

        Notes:
            • Возвращает доступные таймслоты в заданном интервале и часовой пояс склада.
            • Если таймслотов нет, заполняется `reasons` с причинами.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectGetTimeslot

        Args:
            request: Параметры поиска таймслотов по схеме
                `FbpDraftDirectTimeslotGetRequest`

        Returns:
            Список таймслотов по схеме `FbpDraftDirectTimeslotGetResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_timeslot_get(
                    FbpDraftDirectTimeslotGetRequest(
                        bundle_id="bundle-1",
                        warehouse_id=123,
                        interval_start="2026-06-10T00:00:00Z",
                        interval_end="2026-06-12T00:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/timeslot/get",
            payload=request.model_dump(),
        )
        return FbpDraftDirectTimeslotGetResponse(**response)
