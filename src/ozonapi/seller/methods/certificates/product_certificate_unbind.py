from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateUnbindRequest,
    ProductCertificateUnbindResponse,
)


class ProductCertificateUnbindMixin(APIManager):
    """Реализует метод /v1/product/certificate/unbind"""

    async def product_certificate_unbind(
            self: "ProductCertificateUnbindMixin",
            request: ProductCertificateUnbindRequest
    ) -> ProductCertificateUnbindResponse:
        """Метод для отвязки товара от сертификата.

        Notes:
            • Отвязывает указанные товары от сертификата; по каждому товару возвращается результат.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateUnbind

        Args:
            request: Запрос на отвязку товара по схеме `ProductCertificateUnbindRequest`

        Returns:
            Результат отвязки по схеме `ProductCertificateUnbindResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_unbind(
                    ProductCertificateUnbindRequest(
                        certificate_id=50058,
                        product_id=["123456"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/unbind",
            payload=request.model_dump()
        )
        return ProductCertificateUnbindResponse(**response)
