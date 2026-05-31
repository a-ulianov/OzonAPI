import pytest

from src.ozonapi.seller.schemas.reviews import ReviewListV1Request, ReviewListV1Response


class TestReviewListV1:
    """Тесты для метода review_list_v1."""

    @pytest.mark.asyncio
    async def test_review_list_v1(self, api, mock_api_request):
        """Тестирует метод review_list_v1."""

        mock_response_data = {
            "has_next": False,
            "last_id": "",
            "reviews": [
                {"id": "r-1", "sku": 987654, "rating": 3, "status": "PROCESSED"}
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReviewListV1Request(limit=100, status="ALL")

        response = await api.review_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewListV1Response)
        assert response.reviews[0].rating == 3
