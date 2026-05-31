from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateProductsListRequest,
    ProductCertificateProductsListResponse,
)


class ProductCertificateProductsListMixin(APIManager):
    """Реализует метод /v1/product/certificate/products/list"""

    async def product_certificate_products_list(
            self: "ProductCertificateProductsListMixin",
            request: ProductCertificateProductsListRequest
    ) -> ProductCertificateProductsListResponse:
        """Метод для получения списка товаров, привязанных к сертификату.

        Notes:
            • Возвращает товары, привязанные к сертификату, со статусом проверки.
            • Постраничный вывод через `page` и `page_size`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateProductsList

        Args:
            request: Запрос на получение списка товаров по схеме `ProductCertificateProductsListRequest`

        Returns:
            Список товаров по схеме `ProductCertificateProductsListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_products_list(
                    ProductCertificateProductsListRequest(
                        certificate_id=50058,
                        page=1,
                        page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/products/list",
            payload=request.model_dump()
        )
        return ProductCertificateProductsListResponse(**response)
