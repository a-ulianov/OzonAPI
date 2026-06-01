from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffRegistrateRequest,
    FbpDraftDropOffRegistrateResponse,
)


class FbpDraftDropOffRegistrateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/registrate"""

    async def fbp_draft_drop_off_registrate(
            self: "FbpDraftDropOffRegistrateMixin",
            request: FbpDraftDropOffRegistrateRequest,
    ) -> FbpDraftDropOffRegistrateResponse:
        """Переводит drop-off черновик в действующую поставку.

        Notes:
            • При наличии ошибок `is_error=true`; детали — в `error.order_error`
              и `error.bundle_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffRegistrate

        Args:
            request: Параметры регистрации по схеме `FbpDraftDropOffRegistrateRequest`

        Returns:
            Результат регистрации по схеме `FbpDraftDropOffRegistrateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_registrate(
                    FbpDraftDropOffRegistrateRequest(supply_id="55", row_version=1)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/registrate",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffRegistrateResponse(**response)
