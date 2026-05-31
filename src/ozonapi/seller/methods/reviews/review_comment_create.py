from ...core import APIManager
from ...schemas.reviews import ReviewCommentCreateRequest, ReviewCommentCreateResponse


class ReviewCommentCreateMixin(APIManager):
    """Реализует метод /v1/review/comment/create"""

    async def review_comment_create(
            self: "ReviewCommentCreateMixin",
            request: ReviewCommentCreateRequest
    ) -> ReviewCommentCreateResponse:
        """Метод для создания комментария к отзыву.

        Notes:
            • Оставляет комментарий к отзыву; можно ответить на другой комментарий через
              `parent_comment_id` и перевести отзыв в «Обработанный» через `mark_review_as_processed`.
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_CommentCreate

        Args:
            request: Запрос на создание комментария по схеме `ReviewCommentCreateRequest`

        Returns:
            Идентификатор комментария по схеме `ReviewCommentCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_comment_create(
                    ReviewCommentCreateRequest(
                        review_id="abc",
                        text="Спасибо за отзыв!"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/comment/create",
            payload=request.model_dump()
        )
        return ReviewCommentCreateResponse(**response)
