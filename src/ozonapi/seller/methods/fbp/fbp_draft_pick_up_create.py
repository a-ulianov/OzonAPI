from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftPickUpCreateRequest,
    FbpDraftPickUpCreateResponse,
)


class FbpDraftPickUpCreateMixin(APIManager):
    """Реализует метод /v1/fbp/draft/pick-up/create"""

    async def fbp_draft_pick_up_create(
            self: "FbpDraftPickUpCreateMixin",
            request: FbpDraftPickUpCreateRequest,
    ) -> FbpDraftPickUpCreateResponse:
        """Создаёт черновик заявки на pick-up поставку.

        Notes:
            • Указываются данные точки забора (адрес, дата, отправитель).

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftPickupCreate

        Args:
            request: Параметры создания по схеме `FbpDraftPickUpCreateRequest`

        Returns:
            Идентификаторы черновика и поставки по схеме `FbpDraftPickUpCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_pick_up_create(
                    FbpDraftPickUpCreateRequest(
                        bundle_id="b1",
                        delivery_details=FbpPickUpDeliveryDetails(
                            address="Москва, ул. Тестовая, 1",
                            comment="Звонить заранее",
                            date="2026-06-10T10:00:00Z",
                            sender_name="Иванов И.И.",
                            sender_phone="+79990000000",
                        ),
                        package_units_count=1,
                        warehouse_id=123,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/create",
            payload=request.model_dump(),
        )
        return FbpDraftPickUpCreateResponse(**response)
