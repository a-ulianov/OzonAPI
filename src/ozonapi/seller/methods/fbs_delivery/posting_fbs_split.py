from ...core import APIManager
from ...schemas.fbs_delivery import PostingFBSSplitRequest, PostingFBSSplitResponse


class PostingFBSSplitMixin(APIManager):
    """Реализует метод /v1/posting/fbs/split"""

    async def posting_fbs_split(
            self: "PostingFBSSplitMixin",
            request: PostingFBSSplitRequest
    ) -> PostingFBSSplitResponse:
        """Метод для разделения заказа на отправления без сборки.

        Notes:
            • Делит исходное отправление на несколько по указанному составу товаров.
            • В ответе возвращается исходное отправление (`parent_posting`) и список
              новых отправлений (`postings`).

        References:
            https://docs.ozon.ru/api/seller/#operation/PostingAPI_SplitPosting

        Args:
            request: Запрос на разделение заказа по схеме `PostingFBSSplitRequest`

        Returns:
            Результат разделения заказа по схеме `PostingFBSSplitResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.posting_fbs_split(
                    PostingFBSSplitRequest(
                        posting_number="33920113-1231-1",
                        postings=[
                            PostingFBSSplitRequestPosting(
                                products=[ProductFbsSplit(product_id=123, quantity=1)]
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="posting/fbs/split",
            payload=request.model_dump()
        )
        return PostingFBSSplitResponse(**response)
