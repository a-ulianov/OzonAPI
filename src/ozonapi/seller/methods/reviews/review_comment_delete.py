from ...core import APIManager
from ...schemas.reviews import ReviewCommentDeleteRequest, ReviewCommentDeleteResponse


class ReviewCommentDeleteMixin(APIManager):
    """Реализует метод /v2/review/comment/delete"""

    async def review_comment_delete(
            self: "ReviewCommentDeleteMixin",
            request: ReviewCommentDeleteRequest
    ) -> ReviewCommentDeleteResponse:
        """Метод для удаления комментария к отзыву (v2).

        Notes:
            • Удаляет комментарий продавца по идентификатору комментария и SKU товара.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_CommentDeleteV2

        Args:
            request: Запрос на удаление комментария по схеме `ReviewCommentDeleteRequest`

        Returns:
            Результат удаления комментария по схеме `ReviewCommentDeleteResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_comment_delete(
                    ReviewCommentDeleteRequest(
                        comment_id="abc",
                        sku=987654
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="review/comment/delete",
            payload=request.model_dump()
        )
        return ReviewCommentDeleteResponse(**response)
