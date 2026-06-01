from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDropOffDlvEditRequest,
    FbpOrderDropOffDlvEditResponse,
)


class FbpOrderDropOffDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/order/drop-off/dlv/edit"""

    async def fbp_order_drop_off_dlv_edit(
            self: "FbpOrderDropOffDlvEditMixin",
            request: FbpOrderDropOffDlvEditRequest,
    ) -> FbpOrderDropOffDlvEditResponse:
        """Редактирует информацию о поставке на drop-off пункт.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderDropOffDlvEdit

        Args:
            request: Параметры редактирования по схеме `FbpOrderDropOffDlvEditRequest`

        Returns:
            Обновлённая версия записи по схеме `FbpOrderDropOffDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_drop_off_dlv_edit(
                    FbpOrderDropOffDlvEditRequest(
                        supply_id="70",
                        row_version=1,
                        drop_off_date="2026-06-11T10:00:00Z",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/drop-off/dlv/edit",
            payload=request.model_dump(),
        )
        return FbpOrderDropOffDlvEditResponse(**response)
