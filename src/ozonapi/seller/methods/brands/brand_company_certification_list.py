from ...core import APIManager
from ...schemas.brands import (
    BrandCompanyCertificationListRequest,
    BrandCompanyCertificationListResponse,
)


class BrandCompanyCertificationListMixin(APIManager):
    """Реализует метод /v1/brand/company-certification/list"""

    async def brand_company_certification_list(
            self: "BrandCompanyCertificationListMixin",
            request: BrandCompanyCertificationListRequest = BrandCompanyCertificationListRequest(),
    ) -> BrandCompanyCertificationListResponse:
        """Метод для получения списка сертифицируемых брендов.

        Notes:
            • Возвращает список брендов с признаком необходимости сертификата
              (`has_certificate`).
            • Список брендов, для которых нужен сертификат, не статичен и может
              меняться.
            • Использует постраничную пагинацию (`page`, `page_size`).

        References:
            https://docs.ozon.ru/api/seller/?#operation/BrandAPI_BrandCompanyCertificationList

        Args:
            request: Параметры пагинации по схеме `BrandCompanyCertificationListRequest`

        Returns:
            Список сертифицируемых брендов по схеме
            `BrandCompanyCertificationListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.brand_company_certification_list(
                    BrandCompanyCertificationListRequest(page=1, page_size=100)
                )

            total = result.result.total
            for brand in result.result.brand_certification:
                print(brand.brand_name, brand.has_certificate)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="brand/company-certification/list",
            payload=request.model_dump(),
        )
        return BrandCompanyCertificationListResponse(**response)
