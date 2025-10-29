from ...core import APIManager
from ...schemas.fbs_assembly_and_labeling import (
    FBSPostingProductExemplarCreateOrGetRequest,
    FBSPostingProductExemplarCreateOrGetResponse
)


class FBSPostingProductExemplarCreateOrGetMixin(APIManager):
    """Реализует метод /v6/fbs/posting/product/exemplar/create-or-get"""

    async def fbs_posting_product_exemplar_create_or_get(
            self: "FBSPostingProductExemplarCreateOrGetMixin",
            request: FBSPostingProductExemplarCreateOrGetRequest
    ) -> FBSPostingProductExemplarCreateOrGetResponse:
        """Метод для получения информации по экземплярам товаров из отправления, переданных в методе `/v6/fbs/posting/product/exemplar/set`.

        Notes:
            • Метод возвращает данные о созданных экземплярах товаров в отправлении.
            • Используйте метод для получения `exemplar_id` созданных экземпляров.
            • Метод возвращает информацию о количестве коробок, список товаров и их экземпляров.
            • Для весовых товаров возвращаются минимальный и максимальный вес экземпляра.
            • Для каждого экземпляра возвращаются данные о маркировках, весе и идентификаторах.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_FbsPostingProductExemplarCreateOrGetV6

        Args:
            request: Запрос на получение информации о созданных экземплярах по схеме `FBSPostingProductExemplarCreateOrGetRequest`

        Returns:
            Ответ с информацией о созданных экземплярах по схеме `FBSPostingProductExemplarCreateOrGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbs_posting_product_exemplar_create_or_get(
                    FBSPostingProductExemplarCreateOrGetRequest(
                        posting_number="43658312-0011-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v6",
            endpoint="fbs/posting/product/exemplar/create-or-get",
            payload=request.model_dump()
        )
        return FBSPostingProductExemplarCreateOrGetResponse(**response)