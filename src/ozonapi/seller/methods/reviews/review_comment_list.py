from ...core import APIManager
from ...schemas.reviews import ReviewCommentListRequest, ReviewCommentListResponse


class ReviewCommentListMixin(APIManager):
    """Реализует метод /v1/review/comment/list"""

    async def review_comment_list(
            self: "ReviewCommentListMixin",
            request: ReviewCommentListRequest
    ) -> ReviewCommentListResponse:
        """Метод для получения списка комментариев к отзыву.

        Notes:
            • Возвращает комментарии к отзыву с информацией о статусе, лайках и модерации.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_CommentList

        Args:
            request: Запрос на получение списка комментариев по схеме `ReviewCommentListRequest`

        Returns:
            Список комментариев по схеме `ReviewCommentListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_comment_list(
                    ReviewCommentListRequest(
                        review_id="abc",
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/comment/list",
            payload=request.model_dump()
        )
        return ReviewCommentListResponse(**response)
