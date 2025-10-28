from ...core import APIManager
from ...schemas.fbs import PostingFBSProductChangeRequest, PostingFBSProductChangeResponse


class PostingFBSProductChangeMixin(APIManager):
    """Реализует метод /v2/posting/fbs/product/change"""

    async def posting_fbs_product_change(
            self: "PostingFBSProductChangeMixin",
            request: PostingFBSProductChangeRequest
    ) -> PostingFBSProductChangeResponse:
        """Метод для добавления веса для весовых товаров в отправлении FBS.

        Notes:
            • Метод используется для указания фактического веса весовых товаров в отправлении.
            • Можно указать вес для нескольких товаров в одном запросе.
            • После указания веса система пересчитывает стоимость доставки и другие параметры отправления.

        References:
            https://docs.ozon.ru/api/seller/?__rr=1#operation/PostingAPI_ChangeFbsPostingProduct

        Args:
            request: Запрос на добавление веса для весовых товаров в отправлении по схеме `PostingFBSProductChangeRequest`

        Returns:
            Результат выполнения операции по схеме `PostingFBSProductChangeResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_product_change(
                    PostingFBSProductChangeRequest(
                        posting_number="33920158-0006-1",
                        items=[
                            PostingFBSProductChangeRequestItem(
                                sku=1231428352,
                                weight_real=0.3
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/product/change",
            payload=request.model_dump(by_alias=True)
        )
        return PostingFBSProductChangeResponse(**response)
