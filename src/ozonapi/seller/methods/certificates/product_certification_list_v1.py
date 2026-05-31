from ...core import APIManager
from ...schemas.certificates import (
    ProductCertificationListV1Request,
    ProductCertificationListV1Response,
)


class ProductCertificationListV1Mixin(APIManager):
    """Реализует метод /v1/product/certification/list"""

    async def product_certification_list_v1(
            self: "ProductCertificationListV1Mixin",
            request: ProductCertificationListV1Request
    ) -> ProductCertificationListV1Response:
        """Метод для получения списка сертифицируемых категорий (версия 1).

        Notes:
            • Устаревшая версия; для новых интеграций используйте `product_certification_list()` (v2).

        References:
            https://docs.ozon.ru/api/seller/#operation/ProductAPI_ProductCertificationList

        Args:
            request: Запрос на получение списка категорий по схеме `ProductCertificationListV1Request`

        Returns:
            Список сертифицируемых категорий по схеме `ProductCertificationListV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.product_certification_list_v1(
                    ProductCertificationListV1Request(
                        page=1,
                        page_size=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="product/certification/list",
            payload=request.model_dump()
        )
        return ProductCertificationListV1Response(**response)
