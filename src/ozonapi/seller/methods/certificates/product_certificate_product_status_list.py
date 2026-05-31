from ...core import APIManager
from ...schemas.certificates import ProductCertificateProductStatusListResponse


class ProductCertificateProductStatusListMixin(APIManager):
    """Реализует метод /v1/product/certificate/product_status/list"""

    async def product_certificate_product_status_list(
            self: "ProductCertificateProductStatusListMixin"
    ) -> ProductCertificateProductStatusListResponse:
        """Метод для получения списка возможных статусов товаров.

        Notes:
            • Возвращает справочник статусов товаров при привязке к сертификату.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateProductStatusList

        Returns:
            Список статусов товаров по схеме `ProductCertificateProductStatusListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_product_status_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/product_status/list",
            payload={}
        )
        return ProductCertificateProductStatusListResponse(**response)
