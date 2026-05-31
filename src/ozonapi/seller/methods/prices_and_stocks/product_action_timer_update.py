from ...core import APIManager
from ...schemas.prices_and_stocks import (
    ProductActionTimerUpdateRequest,
    ProductActionTimerUpdateResponse,
)


class ProductActionTimerUpdateMixin(APIManager):
    """Реализует метод /v1/product/action/timer/update"""

    async def product_action_timer_update(
            self: "ProductActionTimerUpdateMixin",
            request: ProductActionTimerUpdateRequest,
    ) -> ProductActionTimerUpdateResponse:
        """Обновляет таймер актуальности минимальной цены для указанных товаров.

        Notes:
            • Таймер задаёт период, в течение которого минимальная цена товара считается актуальной.
            • Используйте метод, чтобы продлить актуальность минимальной цены и сохранить участие
              товара в автоматических акциях.
            • За один запрос можно передать до 1000 идентификаторов товаров.
            • Текущий статус таймера можно получить методом `product_action_timer_status()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductActionTimerUpdate

        Args:
            request: Идентификаторы товаров для обновления таймера по схеме `ProductActionTimerUpdateRequest`

        Returns:
            Результат обновления таймера по схеме `ProductActionTimerUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_action_timer_update(
                    ProductActionTimerUpdateRequest(
                        product_ids=["313455276"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/action/timer/update",
            payload=request.model_dump(),
        )
        return ProductActionTimerUpdateResponse(**response)
