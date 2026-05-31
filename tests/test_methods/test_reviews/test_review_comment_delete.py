import pytest

from src.ozonapi.seller.schemas.reviews import ReviewCommentDeleteRequest, ReviewCommentDeleteResponse


class TestReviewCommentDelete:
    """Тесты для метода review_comment_delete."""

    @pytest.mark.asyncio
    async def test_review_comment_delete(self, api, mock_api_request):
        """Тестирует метод review_comment_delete."""

        mock_api_request.return_value = {}

        request = ReviewCommentDeleteRequest(comment_id="c-1", sku=987654)

        response = await api.review_comment_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="review/comment/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewCommentDeleteResponse)
