from ...core import APIManager
from ...schemas.products import ProductListRequest, ProductListResponse


class ProductListMixin(APIManager):
    """Реализует метод /v3/product/list"""

    async def product_list(
        self: "ProductListMixin",
        request: ProductListRequest = ProductListRequest.model_construct()
    ) -> ProductListResponse:
        """Получает список всех товаров продавца.

        Notes:
            • Можно использовать без параметров - выводит всё по максимальному лимиту.
            • Если вы используете фильтр по идентификатору `offer_id` или `product_id`, остальные параметры заполнять не обязательно.
            • За один раз можно использовать только одну группу идентификаторов, не больше 1000 товаров.
            • Для пагинации используйте параметр `last_id` из ответа предыдущего запроса.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1&abt_att=1#operation/ProductAPI_GetProductList

        Args:
            request: Фильтр и параметры пагинации для получения списка товаров по схеме `ProductListRequest`.

        Returns:
            Список товаров с информацией об остатках и пагинацией по схеме `ProductListResponse`.

        Example:
            Базовый пример выборки:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_list()

            Пример выборки с фильтрацией:
                async with SellerAPI(client_id, api_key) as api:
                    result = await api.product_list(
                        ProductListRequest(
                            filter=ProductListFilter(
                                offer_id=["136748"],
                                product_id=[223681945],
                                visibility=Visibility.ALL
                            ),
                            limit=100,
                            last_id=""
                        ),
                    )
        """
        response = await self._request(
            method="post",
            api_version="v3",
            endpoint="product/list",
            payload=request.model_dump(),
        )
        return ProductListResponse(**response)
