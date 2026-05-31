from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateListRequest,
    ProductCertificateListResponse,
)


class ProductCertificateListMixin(APIManager):
    """Реализует метод /v1/product/certificate/list"""

    async def product_certificate_list(
            self: "ProductCertificateListMixin",
            request: ProductCertificateListRequest
    ) -> ProductCertificateListResponse:
        """Метод для получения списка сертификатов.

        Notes:
            • Возвращает сертификаты продавца с фильтрацией по товару, статусу и типу.
            • Постраничный вывод через `page` и `page_size`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateList

        Args:
            request: Запрос на получение списка сертификатов по схеме `ProductCertificateListRequest`

        Returns:
            Список сертификатов по схеме `ProductCertificateListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_list(
                    ProductCertificateListRequest(
                        page=1,
                        page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/list",
            payload=request.model_dump()
        )
        return ProductCertificateListResponse(**response)
