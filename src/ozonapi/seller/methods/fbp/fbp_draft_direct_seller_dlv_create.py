from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDirectSellerDlvCreateRequest,
    FbpDraftDirectSellerDlvCreateResponse,
)


class FbpDraftDirectSellerDlvCreateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/direct/seller-dlv/create"""

    async def fbp_draft_direct_seller_dlv_create(
            self: "FbpDraftDirectSellerDlvCreateMixin",
            request: FbpDraftDirectSellerDlvCreateRequest,
    ) -> FbpDraftDirectSellerDlvCreateResponse:
        """Создаёт черновик заявки на поставку с доставкой силами продавца.

        Notes:
            • Указываются данные водителя и транспортного средства, а также таймслот.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDirectSellerDlvCreate

        Args:
            request: Параметры создания по схеме `FbpDraftDirectSellerDlvCreateRequest`

        Returns:
            Идентификаторы черновика и поставки по схеме
            `FbpDraftDirectSellerDlvCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_direct_seller_dlv_create(
                    FbpDraftDirectSellerDlvCreateRequest(
                        bundle_id="bundle-1",
                        delivery_details=FbpDraftDirectSellerDlvCreateDeliveryDetails(
                            driver_name="Иванов И.И.",
                            timeslot_start="2026-06-10T10:00:00Z",
                            vehicle_number="А123ВС777",
                            vehicle_type="Грузовой",
                        ),
                        package_units_count=1,
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/direct/seller-dlv/create",
            payload=request.model_dump(),
        )
        return FbpDraftDirectSellerDlvCreateResponse(**response)
