from ...core import APIManager
from ...schemas.certificates import ProductCertificateAccordanceTypesListResponse


class ProductCertificateAccordanceTypesListMixin(APIManager):
    """Реализует метод /v2/product/certificate/accordance-types/list"""

    async def product_certificate_accordance_types_list(
            self: "ProductCertificateAccordanceTypesListMixin"
    ) -> ProductCertificateAccordanceTypesListResponse:
        """Метод для получения списка типов соответствия требованиям (версия 2).

        Notes:
            • Возвращает основные типы соответствия и типы для опасных товаров.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateAccordanceTypesV2

        Returns:
            Типы соответствия требованиям по схеме `ProductCertificateAccordanceTypesListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_accordance_types_list()
        """
        response = await self._request(
            method="get",
            api_version="v2",
            endpoint="product/certificate/accordance-types/list",
            payload={}
        )
        return ProductCertificateAccordanceTypesListResponse(**response)
