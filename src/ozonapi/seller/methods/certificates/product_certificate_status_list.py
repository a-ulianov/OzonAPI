from ...core import APIManager
from ...schemas.certificates import ProductCertificateStatusListResponse


class ProductCertificateStatusListMixin(APIManager):
    """Реализует метод /v1/product/certificate/status/list"""

    async def product_certificate_status_list(
            self: "ProductCertificateStatusListMixin"
    ) -> ProductCertificateStatusListResponse:
        """Метод для получения возможных статусов сертификатов.

        Notes:
            • Возвращает справочник возможных статусов сертификатов.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateStatusList

        Returns:
            Список возможных статусов сертификатов по схеме `ProductCertificateStatusListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_status_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/status/list",
            payload={}
        )
        return ProductCertificateStatusListResponse(**response)
