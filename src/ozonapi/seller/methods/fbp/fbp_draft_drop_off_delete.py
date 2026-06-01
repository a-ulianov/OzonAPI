from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffDeleteRequest,
    FbpDraftDropOffDeleteResponse,
)


class FbpDraftDropOffDeleteMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/delete"""

    async def fbp_draft_drop_off_delete(
            self: "FbpDraftDropOffDeleteMixin",
            request: FbpDraftDropOffDeleteRequest,
    ) -> FbpDraftDropOffDeleteResponse:
        """Удаляет черновик для доставки в drop-off пункт.

        Notes:
            • Возвращает состояние отмены и обновлённую версию записи.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffDelete

        Args:
            request: Идентификатор поставки по схеме `FbpDraftDropOffDeleteRequest`

        Returns:
            Состояние отмены по схеме `FbpDraftDropOffDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_delete(
                    FbpDraftDropOffDeleteRequest(supply_id="55")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/delete",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffDeleteResponse(**response)
