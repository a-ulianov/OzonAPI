from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectTplDlvCreateRequest,
    FbpDraftDirectTplDlvCreateResponse,
)


class FbpDraftDirectTplDlvCreateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/tpl-dlv/create"""

    async def fbp_draft_direct_tpl_dlv_create(
            self: "FbpDraftDirectTplDlvCreateMixin",
            request: FbpDraftDirectTplDlvCreateRequest,
    ) -> FbpDraftDirectTplDlvCreateResponse:
        """Создаёт черновик заявки на доставку сторонней транспортной компанией.

        Notes:
            • Указываются трек-номер и название транспортной компании, а также таймслот.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectTplDlvCreate

        Args:
            request: Параметры создания по схеме `FbpDraftDirectTplDlvCreateRequest`

        Returns:
            Идентификаторы черновика и поставки по схеме
            `FbpDraftDirectTplDlvCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_tpl_dlv_create(
                    FbpDraftDirectTplDlvCreateRequest(
                        bundle_id="bundle-1",
                        delivery_details=FbpDraftDirectTplDlvCreateDeliveryDetails(
                            timeslot_start="2026-06-10T10:00:00Z",
                            tracking_number="TRK-123",
                            transport_company_name="СДЭК",
                        ),
                        package_units_count=1,
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/tpl-dlv/create",
            payload=request.model_dump(),
        )
        return FbpDraftDirectTplDlvCreateResponse(**response)
