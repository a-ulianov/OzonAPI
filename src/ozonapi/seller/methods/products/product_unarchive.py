from ...core import APIManager
from ...schemas.products import ProductUnarchiveRequest, ProductUnarchiveResponse


class ProductUnarchiveMixin(APIManager):
    """Реализует метод /v1/product/unarchive"""

    async def product_unarchive(
        self: "ProductUnarchiveMixin",
        request: ProductUnarchiveRequest
    ) -> ProductUnarchiveResponse:
        """Восстанавливает товары из архива.

        Notes:
            • В одном запросе можно передать до `100` идентификаторов товаров.
            • В сутки можно восстановить из архива не больше `10` товаров, которые были архивированы автоматически.
            • Лимит обновляется в `03:00` по московскому времени.
            • На разархивацию товаров, перенесённых в архив вручную, ограничений нет.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_ProductUnarchive

        Args:
            request: Список `product_id` для восстановления из архива по схеме `ProductUnarchiveRequest`.

        Returns:
            Результат обработки запроса по схеме `ProductUnarchiveResponse`.

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_unarchive(
                    ProductUnarchiveRequest(
                        product_id=[125529926]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/unarchive",
            payload=request.model_dump(),
        )
        return ProductUnarchiveResponse(**response)
