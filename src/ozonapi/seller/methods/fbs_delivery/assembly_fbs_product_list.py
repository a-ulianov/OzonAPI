from ...core import APIManager
from ...schemas.fbs_delivery import (
    AssemblyFbsProductListRequest,
    AssemblyFbsProductListResponse,
)


class AssemblyFbsProductListMixin(APIManager):
    """Реализует метод /v1/assembly/fbs/product/list"""

    async def assembly_fbs_product_list(
            self: "AssemblyFbsProductListMixin",
            request: AssemblyFbsProductListRequest
    ) -> AssemblyFbsProductListResponse:
        """Метод для получения списка товаров в отправлениях.

        Notes:
            • Возвращает товары, доступные для сборки, с разбивкой по отправлениям.
            • Использует offset-пагинацию (`limit` + `offset`); `has_next` указывает на
              наличие следующей страницы.
            • Направление сортировки задаётся параметром `sort_dir` (`ASC`/`DESC`).
            • В фильтре необходимо передать `cutoff_from` и `cutoff_to`; фильтровать
              рекомендуется по ним (передача `delivery_method_id` может вызывать
              ошибку на стороне Ozon).

        References:
            https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyFbsProductList

        Args:
            request: Запрос на получение списка товаров по схеме `AssemblyFbsProductListRequest`

        Returns:
            Список товаров в отправлениях по схеме `AssemblyFbsProductListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.assembly_fbs_product_list(
                    AssemblyFbsProductListRequest(
                        filter=AssemblyFbsProductListFilter(),
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="assembly/fbs/product/list",
            payload=request.model_dump()
        )
        return AssemblyFbsProductListResponse(**response)
