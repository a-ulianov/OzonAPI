from ...core import APIManager
from ...schemas.certificates import ProductCertificateAccordanceTypesResponse


class ProductCertificateAccordanceTypesMixin(APIManager):
    """Реализует метод /v1/product/certificate/accordance-types"""

    async def product_certificate_accordance_types(
            self: "ProductCertificateAccordanceTypesMixin"
    ) -> ProductCertificateAccordanceTypesResponse:
        """Метод для получения списка типов соответствия требованиям (версия 1).

        Notes:
            • Возвращает справочник типов соответствия требованиям.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateAccordanceTypes

        Returns:
            Список типов соответствия требованиям по схеме `ProductCertificateAccordanceTypesResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_accordance_types()
        """
        response = await self._request(
            method="get",
            api_version="v1",
            endpoint="product/certificate/accordance-types",
            payload={}
        )
        return ProductCertificateAccordanceTypesResponse(**response)
