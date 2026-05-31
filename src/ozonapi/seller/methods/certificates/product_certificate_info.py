from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificateInfoRequest,
    ProductCertificateInfoResponse,
)


class ProductCertificateInfoMixin(APIManager):
    """Реализует метод /v1/product/certificate/info"""

    async def product_certificate_info(
            self: "ProductCertificateInfoMixin",
            request: ProductCertificateInfoRequest
    ) -> ProductCertificateInfoResponse:
        """Метод для получения информации о сертификате.

        Notes:
            • Возвращает подробную информацию о сертификате по его номеру.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateInfo

        Args:
            request: Запрос на получение информации о сертификате по схеме `ProductCertificateInfoRequest`

        Returns:
            Информация о сертификате по схеме `ProductCertificateInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_info(
                    ProductCertificateInfoRequest(
                        certificate_number="RU-123"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/info",
            payload=request.model_dump()
        )
        return ProductCertificateInfoResponse(**response)
