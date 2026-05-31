import pytest

from src.ozonapi.seller.schemas.reviews import ReviewInfoRequest, ReviewInfoResponse


class TestReviewInfo:
    """Тесты для метода review_info."""

    @pytest.mark.asyncio
    async def test_review_info(self, api, mock_api_request):
        """Тестирует метод review_info."""

        mock_response_data = {
            "id": "r-1",
            "sku": 987654,
            "text": "Отличный товар",
            "rating": 5,
            "status": "PROCESSED",
            "photos": [{"url": "http://img", "width": 100, "height": 200}],
            "photos_amount": 1,
            "videos_amount": 0
        }
        mock_api_request.return_value = mock_response_data

        request = ReviewInfoRequest(review_id="r-1")

        response = await api.review_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="review/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewInfoResponse)
        assert response.rating == 5
        assert response.photos[0].width == 100
