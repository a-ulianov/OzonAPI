import pytest

from src.ozonapi.seller.schemas.reviews import (
    ReviewCommentDeleteV1Request,
    ReviewCommentDeleteV1Response,
)


class TestReviewCommentDeleteV1:
    """Тесты для метода review_comment_delete_v1."""

    @pytest.mark.asyncio
    async def test_review_comment_delete_v1(self, api, mock_api_request):
        """Тестирует метод review_comment_delete_v1."""

        mock_api_request.return_value = {}

        request = ReviewCommentDeleteV1Request(comment_id="c-1")

        response = await api.review_comment_delete_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/comment/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewCommentDeleteV1Response)
