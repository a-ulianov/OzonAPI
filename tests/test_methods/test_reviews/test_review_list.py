import pytest

from src.ozonapi.seller.schemas.reviews import ReviewListRequest, ReviewListResponse


class TestReviewList:
    """Тесты для метода review_list."""

    @pytest.mark.asyncio
    async def test_review_list(self, api, mock_api_request):
        """Тестирует метод review_list."""

        mock_response_data = {
            "has_next": True,
            "last_id": "r-2",
            "reviews": [
                {"id": "r-1", "sku": 987654, "rating": 5, "status": "UNPROCESSED", "comments_amount": 0}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReviewListRequest(limit=100)

        response = await api.review_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="review/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewListResponse)
        assert response.has_next is True
        assert response.reviews[0].id == "r-1"
