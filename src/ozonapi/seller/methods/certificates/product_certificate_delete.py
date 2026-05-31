from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateDeleteRequest,
    ProductCertificateDeleteResponse,
)


class ProductCertificateDeleteMixin(APIManager):
    """Реализует метод /v1/product/certificate/delete"""

    async def product_certificate_delete(
            self: "ProductCertificateDeleteMixin",
            request: ProductCertificateDeleteRequest
    ) -> ProductCertificateDeleteResponse:
        """Метод для удаления сертификата.

        Notes:
            • Удаляет сертификат по идентификатору.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateDelete

        Args:
            request: Запрос на удаление сертификата по схеме `ProductCertificateDeleteRequest`

        Returns:
            Результат удаления по схеме `ProductCertificateDeleteResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_delete(
                    ProductCertificateDeleteRequest(
                        certificate_id=50058
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/delete",
            payload=request.model_dump()
        )
        return ProductCertificateDeleteResponse(**response)
