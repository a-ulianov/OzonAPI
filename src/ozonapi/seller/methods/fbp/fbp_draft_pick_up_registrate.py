from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftPickUpRegistrateRequest,
    FbpDraftPickUpRegistrateResponse,
)


class FbpDraftPickUpRegistrateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/pick-up/registrate"""

    async def fbp_draft_pick_up_registrate(
            self: "FbpDraftPickUpRegistrateMixin",
            request: FbpDraftPickUpRegistrateRequest,
    ) -> FbpDraftPickUpRegistrateResponse:
        """Переводит pick-up черновик в действующую поставку.

        Notes:
            • При наличии ошибок `is_error=true`; детали — в `error.order_error`
              и `error.bundle_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftPickUpRegistrate

        Args:
            request: Параметры регистрации по схеме `FbpDraftPickUpRegistrateRequest`

        Returns:
            Результат регистрации по схеме `FbpDraftPickUpRegistrateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_pick_up_registrate(
                    FbpDraftPickUpRegistrateRequest(supply_id="60", row_version=1)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/registrate",
            payload=request.model_dump(),
        )
        return FbpDraftPickUpRegistrateResponse(**response)
