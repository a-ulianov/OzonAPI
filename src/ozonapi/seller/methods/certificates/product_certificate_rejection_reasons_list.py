from ...core import APIManager
from ...schemas.certificates import ProductCertificateRejectionReasonsListResponse


class ProductCertificateRejectionReasonsListMixin(APIManager):
    """Реализует метод /v1/product/certificate/rejection_reasons/list"""

    async def product_certificate_rejection_reasons_list(
            self: "ProductCertificateRejectionReasonsListMixin"
    ) -> ProductCertificateRejectionReasonsListResponse:
        """Метод для получения возможных причин отклонения сертификата.

        Notes:
            • Возвращает справочник причин отклонения сертификата.
            • Метод не принимает параметров.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificateRejectionReasonsList

        Returns:
            Причины отклонения сертификата по схеме `ProductCertificateRejectionReasonsListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certificate_rejection_reasons_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certificate/rejection_reasons/list",
            payload={}
        )
        return ProductCertificateRejectionReasonsListResponse(**response)
