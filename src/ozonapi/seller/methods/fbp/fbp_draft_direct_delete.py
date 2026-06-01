from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectDeleteRequest,
    FbpDraftDirectDeleteResponse,
)


class FbpDraftDirectDeleteMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/delete"""

    async def fbp_draft_direct_delete(
            self: "FbpDraftDirectDeleteMixin",
            request: FbpDraftDirectDeleteRequest,
    ) -> FbpDraftDirectDeleteResponse:
        """Удаляет черновик заявки на поставку.

        Notes:
            • Возвращает состояние отмены и обновлённую версию записи.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectDelete

        Args:
            request: Идентификатор поставки по схеме `FbpDraftDirectDeleteRequest`

        Returns:
            Состояние отмены по схеме `FbpDraftDirectDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_delete(
                    FbpDraftDirectDeleteRequest(supply_id="123")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/delete",
            payload=request.model_dump(),
        )
        return FbpDraftDirectDeleteResponse(**response)
