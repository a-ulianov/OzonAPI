from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificationListRequest,
    ProductCertificationListResponse,
)


class ProductCertificationListMixin(APIManager):
    """Реализует метод /v2/product/certification/list"""

    async def product_certification_list(
            self: "ProductCertificationListMixin",
            request: ProductCertificationListRequest
    ) -> ProductCertificationListResponse:
        """Метод для получения списка сертифицируемых категорий (версия 2).

        Notes:
            • Возвращает категории и типы, для которых требуется сертификация.
            • Постраничный вывод через `page` и `page_size`.

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificationListV2

        Args:
            request: Запрос на получение списка категорий по схеме `ProductCertificationListRequest`

        Returns:
            Список сертифицируемых категорий по схеме `ProductCertificationListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certification_list(
                    ProductCertificationListRequest(
                        page=1,
                        page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="product/certification/list",
            payload=request.model_dump()
        )
        return ProductCertificationListResponse(**response)
