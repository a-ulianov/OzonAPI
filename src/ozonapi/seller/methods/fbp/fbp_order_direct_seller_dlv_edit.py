from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDirectSellerDlvEditRequest,
    FbpOrderDirectSellerDlvEditResponse,
)


class FbpOrderDirectSellerDlvEditMixin(APIManager):
    """Реализует метод /v1/fbp/order/direct/seller-dlv/edit"""

    async def fbp_order_direct_seller_dlv_edit(
            self: "FbpOrderDirectSellerDlvEditMixin",
            request: FbpOrderDirectSellerDlvEditRequest,
    ) -> FbpOrderDirectSellerDlvEditResponse:
        """Обновляет информацию о доставке силами продавца в поставке.

        Notes:
            • Для оптимистичной блокировки передавайте актуальный `row_version`.
            • При наличии ошибок `is_error=true`; детали — в `error.order_errors`.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderDirectSellerDlvEdit

        Args:
            request: Параметры обновления по схеме `FbpOrderDirectSellerDlvEditRequest`

        Returns:
            Результат обновления по схеме `FbpOrderDirectSellerDlvEditResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_direct_seller_dlv_edit(
                    FbpOrderDirectSellerDlvEditRequest(
                        supply_id="70",
                        row_version=1,
                        driver_name="Иванов И.И.",
                        vehicle_number="А123ВС777",
                        vehicle_type="Грузовой",
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/direct/seller-dlv/edit",
            payload=request.model_dump(),
        )
        return FbpOrderDirectSellerDlvEditResponse(**response)
