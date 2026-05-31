from ...core import APIManager
from ...schemas.fbs_delivery import (
    AssemblyCarriageProductListRequest,
    AssemblyCarriageProductListResponse,
)


class AssemblyCarriageProductListMixin(APIManager):
    """Реализует метод /v1/assembly/carriage/product/list"""

    async def assembly_carriage_product_list(
            self: "AssemblyCarriageProductListMixin",
            request: AssemblyCarriageProductListRequest
    ) -> AssemblyCarriageProductListResponse:
        """Метод для получения списка товаров в отгрузке.

        Notes:
            • Возвращает товары отгрузки с номерами отправлений, в которых они находятся.
            • Использует курсорную пагинацию: передавайте `cursor` из предыдущего ответа.

        References:
            https://docs.ozon.ru/api/seller/#operation/AssemblyAPI_AssemblyCarriageProductList

        Args:
            request: Запрос на получение списка товаров по схеме `AssemblyCarriageProductListRequest`

        Returns:
            Список товаров в отгрузке по схеме `AssemblyCarriageProductListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.assembly_carriage_product_list(
                    AssemblyCarriageProductListRequest(
                        filter=AssemblyCarriageProductListFilter(carriage_id=12345),
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="assembly/carriage/product/list",
            payload=request.model_dump()
        )
        return AssemblyCarriageProductListResponse(**response)
