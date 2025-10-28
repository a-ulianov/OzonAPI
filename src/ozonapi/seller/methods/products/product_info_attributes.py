from ...core import APIManager
from ...schemas.products import ProductInfoAttributesRequest, ProductInfoAttributesResponse


class ProductInfoAttributesMixin(APIManager):
    """Реализует метод /v4/product/info/attributes"""

    async def product_info_attributes(
        self: "ProductInfoAttributesMixin",
        request: ProductInfoAttributesRequest = ProductInfoAttributesRequest.model_construct(),
    ) -> ProductInfoAttributesResponse:
        """Получает описание характеристик товаров по идентификаторам и видимости.

        Notes:
            • Можно не передавать идентификаторы, фильтр, можно вообще ничего не передавать - выберет всё по максимальному лимиту.
            • Товар можно искать по `offer_id`, `product_id` или `sku`.
            • Можно передавать до `1000` значений в фильтре.
            • Для пагинации используйте параметр `last_id` из ответа предыдущего запроса.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductAttributesV4

        Args:
            request: Фильтр и параметры запроса для получения характеристик товаров по схеме `ProductInfoAttributesRequest`.

        Returns:
            Описание характеристик товаров с пагинацией по схеме `ProductInfoAttributesResponse`.

        Examples:
            Базовый пример использования:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_attributes()

            Пример с фильтрацией выборки:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_info_attributes(
                        ProductInfoAttributesRequest(
                            filter=ProductInfoAttributesFilter(
                                product_id=[213761435],
                                offer_id=["testtest5"],
                                sku=[123495432],
                                visibility=Visibility.ALL
                            ),
                            limit=100,
                            sort_dir=SortingDirection.ASC
                        ),
                    )
        """
        response = await self._request(
            method="post",
            api_version="v4",
            endpoint="product/info/attributes",
            payload=request.model_dump(),
        )
        return ProductInfoAttributesResponse(**response)
