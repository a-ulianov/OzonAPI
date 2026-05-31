from ...core import APIManager
from ...schemas.reviews import (
    ReviewCommentDeleteV1Request,
    ReviewCommentDeleteV1Response,
)


class ReviewCommentDeleteV1Mixin(APIManager):
    """Реализует метод /v1/review/comment/delete"""

    async def review_comment_delete_v1(
            self: "ReviewCommentDeleteV1Mixin",
            request: ReviewCommentDeleteV1Request
    ) -> ReviewCommentDeleteV1Response:
        """Метод для удаления комментария к отзыву (v1).

        Notes:
            • Устаревшая версия; для новых интеграций используйте `review_comment_delete()` (v2).
            • Доступен продавцам с подпиской Premium Plus (раздел Отзывы — beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/Review_CommentDelete

        Args:
            request: Запрос на удаление комментария по схеме `ReviewCommentDeleteV1Request`

        Returns:
            Результат удаления комментария по схеме `ReviewCommentDeleteV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.review_comment_delete_v1(
                    ReviewCommentDeleteV1Request(
                        comment_id="abc"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="review/comment/delete",
            payload=request.model_dump()
        )
        return ReviewCommentDeleteV1Response(**response)
