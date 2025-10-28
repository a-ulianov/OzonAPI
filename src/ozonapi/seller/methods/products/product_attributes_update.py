from ...core import APIManager
from ...schemas.products import ProductAttributesUpdateRequest, ProductAttributesUpdateResponse


class ProductAttributesUpdateMixin(APIManager):
    """Реализует метод /v1/product/attributes/update"""

    async def product_attributes_update(
        self: "ProductAttributesUpdateMixin",
        request: ProductAttributesUpdateRequest
    ) -> ProductAttributesUpdateResponse:
        """Формирует задание на обновление товаров и их характеристик.

        Notes:
            • Запросы обрабатываются очередями.
            • Для получения детализированной информации о результате выполнения операции используйте метод `product_import_info()`.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/ProductAPI_ProductUpdateAttributes

        Args:
            request: Список товарных идентификаторов с характеристиками, которые нужно обновить по схеме `ProductAttributesUpdateRequest`.

        Returns:
            Айдишник таски, результаты выполнения которой затем можно проверить методом `product_import_info()

        Example:
            attributes = [
                ProductAttributesUpdateItemAttribute(
                    complex_id=0, id=1,
                    values=[ProductAttributesUpdateItemAttributeValue(dictionary_value_id=0, value="string"), ]
                ),
            ]

            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_attributes_update(
                    ProductAttributesUpdateRequest(
                        items=[ProductAttributesUpdateItem(offer_id="article-12345", attributes=attributes), ]
                    ),
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/attributes/update",
            payload=request.model_dump(),
        )
        return ProductAttributesUpdateResponse(**response)
