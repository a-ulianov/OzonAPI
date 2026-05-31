from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateBindRequest,
    ProductCertificateBindResponse,
)


class ProductCertificateBindMixin(APIManager):
    """Реализует метод /v1/product/certificate/bind"""

    async def product_certificate_bind(
            self: "ProductCertificateBindMixin",
            request: ProductCertificateBindRequest
    ) -> ProductCertificateBindResponse:
        """Метод для привязки сертификата к товару.

        Notes:
            • Привязывает сертификат к указанным товарам.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateBind

        Args:
            request: Запрос на привязку сертификата по схеме `ProductCertificateBindRequest`

        Returns:
            Результат привязки по схеме `ProductCertificateBindResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_bind(
                    ProductCertificateBindRequest(
                        certificate_id=50058,
                        product_id=[123456]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/bind",
            payload=request.model_dump()
        )
        return ProductCertificateBindResponse(**response)
