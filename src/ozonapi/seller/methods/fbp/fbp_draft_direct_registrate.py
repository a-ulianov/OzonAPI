from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectRegistrateRequest,
    FbpDraftDirectRegistrateResponse,
)


class FbpDraftDirectRegistrateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/registrate"""

    async def fbp_draft_direct_registrate(
            self: "FbpDraftDirectRegistrateMixin",
            request: FbpDraftDirectRegistrateRequest,
    ) -> FbpDraftDirectRegistrateResponse:
        """Переводит черновик в действующую поставку.

        Notes:
            • При наличии ошибок `is_error=true`; детали — в `error.order_error`
              и `error.bundle_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectRegistrate

        Args:
            request: Параметры регистрации по схеме `FbpDraftDirectRegistrateRequest`

        Returns:
            Результат регистрации по схеме `FbpDraftDirectRegistrateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_registrate(
                    FbpDraftDirectRegistrateRequest(supply_id="123", row_version=1)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/registrate",
            payload=request.model_dump(),
        )
        return FbpDraftDirectRegistrateResponse(**response)
