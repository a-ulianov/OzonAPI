from ...core import APIManager
from ...schemas.fbs_delivery import (
    PostingFBSProductTraceableAttributeRequest,
    PostingFBSProductTraceableAttributeResponse,
)


class PostingFBSProductTraceableAttributeMixin(APIManager):
    """Реализует метод /v1/posting/fbs/product/traceable/attribute"""

    async def posting_fbs_product_traceable_attribute(
            self: "PostingFBSProductTraceableAttributeMixin",
            request: PostingFBSProductTraceableAttributeRequest
    ) -> PostingFBSProductTraceableAttributeResponse:
        """Метод для получения списка незаполненных атрибутов прослеживаемых товаров.

        Notes:
            • Возвращает для каждого товара отправления список обязательных атрибутов,
              которые нужно заполнить для прослеживаемых товаров.

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_PostingFbsProductTraceableAttribute

        Args:
            request: Запрос на получение атрибутов по схеме `PostingFBSProductTraceableAttributeRequest`

        Returns:
            Список товаров с обязательными атрибутами по схеме `PostingFBSProductTraceableAttributeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_product_traceable_attribute(
                    PostingFBSProductTraceableAttributeRequest(
                        posting_number="33920113-1231-1"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/product/traceable/attribute",
            payload=request.model_dump()
        )
        return PostingFBSProductTraceableAttributeResponse(**response)
