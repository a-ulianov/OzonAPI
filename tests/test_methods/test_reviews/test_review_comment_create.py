import pytest

from src.ozonapi.seller.schemas.reviews import ReviewCommentCreateRequest, ReviewCommentCreateResponse


class TestReviewCommentCreate:
    """Тесты для метода review_comment_create."""

    @pytest.mark.asyncio
    async def test_review_comment_create(self, api, mock_api_request):
        """Тестирует метод review_comment_create."""

        mock_api_request.return_value = {"comment_id": "c-1"}

        request = ReviewCommentCreateRequest(review_id="r-1", text="Спасибо!")

        response = await api.review_comment_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/comment/create",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewCommentCreateResponse)
        assert response.comment_id == "c-1"
