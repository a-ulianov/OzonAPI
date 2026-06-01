from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffCreateRequest,
    FbpDraftDropOffCreateResponse,
)


class FbpDraftDropOffCreateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/create"""

    async def fbp_draft_drop_off_create(
            self: "FbpDraftDropOffCreateMixin",
            request: FbpDraftDropOffCreateRequest,
    ) -> FbpDraftDropOffCreateResponse:
        """Создаёт черновик для доставки в drop-off пункт.

        Notes:
            • Указываются дата сдачи, идентификатор drop-off пункта и провинции.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffCreate

        Args:
            request: Параметры создания по схеме `FbpDraftDropOffCreateRequest`

        Returns:
            Идентификаторы черновика и поставки по схеме `FbpDraftDropOffCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_create(
                    FbpDraftDropOffCreateRequest(
                        bundle_id="b1",
                        delivery_details=FbpDraftDropOffCreateDeliveryDetails(
                            drop_off_date="2026-06-10T10:00:00Z",
                            drop_off_point_id=7,
                            drop_off_province_uuid="uuid-1",
                        ),
                        package_units_count=1,
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/create",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffCreateResponse(**response)
