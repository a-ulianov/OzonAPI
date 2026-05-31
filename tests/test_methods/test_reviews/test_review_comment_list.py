import pytest

from src.ozonapi.seller.schemas.reviews import ReviewCommentListRequest, ReviewCommentListResponse


class TestReviewCommentList:
    """Тесты для метода review_comment_list."""

    @pytest.mark.asyncio
    async def test_review_comment_list(self, api, mock_api_request):
        """Тестирует метод review_comment_list."""

        mock_response_data = {
            "offset": 1,
            "comments": [
                {"id": "c-1", "text": "Ответ", "is_owner": True, "likes_amount": 2}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReviewCommentListRequest(review_id="r-1", limit=100)

        response = await api.review_comment_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/comment/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewCommentListResponse)
        assert response.comments[0].id == "c-1"
        assert response.comments[0].is_owner is True
