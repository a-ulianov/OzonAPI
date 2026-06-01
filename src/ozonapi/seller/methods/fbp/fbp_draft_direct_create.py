from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectCreateRequest,
    FbpDraftDirectCreateResponse,
)


class FbpDraftDirectCreateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/create"""

    async def fbp_draft_direct_create(
            self: "FbpDraftDirectCreateMixin",
            request: FbpDraftDirectCreateRequest,
    ) -> FbpDraftDirectCreateResponse:
        """Создаёт черновик заявки на поставку без указания способа доставки.

        Notes:
            • Способ доставки уточняется отдельными методами (`seller-dlv`, `tpl-dlv`).
            • В `delivery_details.timeslot_start` передаётся список желаемых таймслотов.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectCreate

        Args:
            request: Параметры создания черновика по схеме `FbpDraftDirectCreateRequest`

        Returns:
            Идентификаторы черновика и поставки по схеме `FbpDraftDirectCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_create(
                    FbpDraftDirectCreateRequest(
                        bundle_id="bundle-1",
                        delivery_details=FbpDraftDirectCreateDeliveryDetails(
                            timeslot_start=["2026-06-10T10:00:00Z"]
                        ),
                        package_units_count=1,
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/create",
            payload=request.model_dump(),
        )
        return FbpDraftDirectCreateResponse(**response)
