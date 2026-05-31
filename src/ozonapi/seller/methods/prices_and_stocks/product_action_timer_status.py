from ...core import APIManager
from ...schemas.prices_and_stocks import (
    ProductActionTimerStatusRequest,
    ProductActionTimerStatusResponse,
)


class ProductActionTimerStatusMixin(APIManager):
    """Реализует метод /v1/product/action/timer/status"""

    async def product_action_timer_status(
            self: "ProductActionTimerStatusMixin",
            request: ProductActionTimerStatusRequest,
    ) -> ProductActionTimerStatusResponse:
        """Получает статус таймера актуальности минимальной цены для указанных товаров.

        Notes:
            • Для каждого товара возвращается время окончания таймера (`expired_at`).
            • Если `expired_at` пустое, активного таймера у товара нет.
            • За один запрос можно передать до 1000 идентификаторов товаров.
            • Обновить таймер можно методом `product_action_timer_update()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductActionTimerStatus

        Args:
            request: Идентификаторы товаров для получения статуса таймера по схеме `ProductActionTimerStatusRequest`

        Returns:
            Список статусов таймеров по запрошенным товарам по схеме `ProductActionTimerStatusResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_action_timer_status(
                    ProductActionTimerStatusRequest(
                        product_ids=["313455276"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/action/timer/status",
            payload=request.model_dump(),
        )
        return ProductActionTimerStatusResponse(**response)
