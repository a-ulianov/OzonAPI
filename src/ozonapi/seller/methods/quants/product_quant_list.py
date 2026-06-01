from ...core import APIManager
from ...schemas.quants import (
    ProductQuantListRequest,
    ProductQuantListResponse,
)


class ProductQuantListMixin(APIManager):
    """Реализует метод /v1/product/quant/list"""

    async def product_quant_list(
            self: "ProductQuantListMixin",
            request: ProductQuantListRequest = ProductQuantListRequest()
    ) -> ProductQuantListResponse:
        """Возвращает список эконом-товаров (квантов) с курсорной пагинацией.

        Notes:
            • Постраничная навигация курсором: передайте `cursor` из предыдущего ответа.
            • Можно отфильтровать товары по видимости через `visibility`.

        References:
            https://docs.ozon.ru/api/seller/#operation/QuantProductList

        Args:
            request: Запрос списка эконом-товаров по схеме `ProductQuantListRequest`

        Returns:
            Список эконом-товаров по схеме `ProductQuantListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_quant_list(
                    ProductQuantListRequest(limit=100, visibility="ALL")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/quant/list",
            payload=request.model_dump()
        )
        return ProductQuantListResponse(**response)
