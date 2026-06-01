from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderPickUpDlvEditRequest,
    FbpOrderPickUpDlvEditResponse,
)


class FbpOrderPickUpDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/order/pick-up/dlv/edit"""

    async def fbp_order_pick_up_dlv_edit(
            self: "FbpOrderPickUpDlvEditMixin",
            request: FbpOrderPickUpDlvEditRequest,
    ) -> FbpOrderPickUpDlvEditResponse:
        """Изменяет данные о точке забора в pick-up поставке.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.
            • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderPickUpDlvEdit

        Args:
            request: Параметры изменения по схеме `FbpOrderPickUpDlvEditRequest`

        Returns:
            Результат изменения по схеме `FbpOrderPickUpDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_pick_up_dlv_edit(
                    FbpOrderPickUpDlvEditRequest(
                        supply_id="70",
                        row_version=1,
                        pickup_details=FbpOrderPickUpEditDetails(
                            sender_name="Иванов И.И.",
                            sender_phone="+79990000000",
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/pick-up/dlv/edit",
            payload=request.model_dump(),
        )
        return FbpOrderPickUpDlvEditResponse(**response)
