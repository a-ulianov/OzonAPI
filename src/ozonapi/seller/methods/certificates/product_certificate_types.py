from ...core import APIManager
from ...schemas.certificates import ProductCertificateTypesResponse


class ProductCertificateTypesMixin(APIManager):
    """Реализует метод /v1/product/certificate/types"""

    async def product_certificate_types(
            self: "ProductCertificateTypesMixin"
    ) -> ProductCertificateTypesResponse:
        """Метод для получения справочника типов документов.

        Notes:
            • Возвращает справочник типов документов (сертификатов).
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateTypes

        Returns:
            Справочник типов документов по схеме `ProductCertificateTypesResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_types()
        """
        response = await self._request(
            method="get",
            api_version="v1",
            endpoint="product/certificate/types",
            payload={}
        )
        return ProductCertificateTypesResponse(**response)
