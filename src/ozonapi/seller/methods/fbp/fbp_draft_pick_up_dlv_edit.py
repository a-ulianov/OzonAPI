from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftPickUpDlvEditRequest,
    FbpDraftPickUpDlvEditResponse,
)


class FbpDraftPickUpDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/draft/pick-up/dlv/edit"""

    async def fbp_draft_pick_up_dlv_edit(
            self: "FbpDraftPickUpDlvEditMixin",
            request: FbpDraftPickUpDlvEditRequest,
    ) -> FbpDraftPickUpDlvEditResponse:
        """Изменяет черновик заявки на pick-up поставку.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftPickupDlvEdit

        Args:
            request: Параметры изменения по схеме `FbpDraftPickUpDlvEditRequest`

        Returns:
            Обновлённая версия записи по схеме `FbpDraftPickUpDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_pick_up_dlv_edit(
                    FbpDraftPickUpDlvEditRequest(
                        supply_id="60",
                        row_version=1,
                        pickup_details=FbpPickUpDeliveryDetails(
                            address="Москва, ул. Тестовая, 1",
                            comment="Звонить заранее",
                            date="2026-06-11T10:00:00Z",
                            sender_name="Иванов И.И.",
                            sender_phone="+79990000000",
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/pick-up/dlv/edit",
            payload=request.model_dump(),
        )
        return FbpDraftPickUpDlvEditResponse(**response)
