from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftPickUpDeleteRequest,
    FbpDraftPickUpDeleteResponse,
)


class FbpDraftPickUpDeleteMixin(APIManager):
    """Реализует метод /v1/fbp/draft/pick-up/delete"""

    async def fbp_draft_pick_up_delete(
            self: "FbpDraftPickUpDeleteMixin",
            request: FbpDraftPickUpDeleteRequest,
    ) -> FbpDraftPickUpDeleteResponse:
        """Отменяет черновик заявки на pick-up поставку.

        Notes:
            • Возвращает состояние отмены и обновлённую версию записи.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftPickUpDelete

        Args:
            request: Идентификатор поставки по схеме `FbpDraftPickUpDeleteRequest`

        Returns:
            Состояние отмены по схеме `FbpDraftPickUpDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_pick_up_delete(
                    FbpDraftPickUpDeleteRequest(supply_id="60")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/delete",
            payload=request.model_dump(),
        )
        return FbpDraftPickUpDeleteResponse(**response)
