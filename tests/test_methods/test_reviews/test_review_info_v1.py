import pytest

from src.ozonapi.seller.schemas.reviews import ReviewInfoV1Request, ReviewInfoV1Response


class TestReviewInfoV1:
    """Тесты для метода review_info_v1."""

    @pytest.mark.asyncio
    async def test_review_info_v1(self, api, mock_api_request):
        """Тестирует метод review_info_v1."""

        mock_response_data = {
            "id": "r-1",
            "sku": 987654,
            "rating": 4,
            "status": "UNPROCESSED",
            "videos": [{"url": "http://vid", "preview_url": "http://prev"}],
            "videos_amount": 1
        }
        mock_api_request.return_value = mock_response_data

        request = ReviewInfoV1Request(review_id="r-1")

        response = await api.review_info_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/info",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewInfoV1Response)
        assert response.rating == 4
        assert response.videos[0].preview_url == "http://prev"
