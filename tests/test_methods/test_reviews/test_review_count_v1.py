import pytest

from src.ozonapi.seller.schemas.reviews import ReviewCountV1Response


class TestReviewCountV1:
    """Тесты для метода review_count_v1."""

    @pytest.mark.asyncio
    async def test_review_count_v1(self, api, mock_api_request):
        """Тестирует метод review_count_v1."""

        mock_api_request.return_value = {"total": 10, "processed": 2, "unprocessed": 8}

        response = await api.review_count_v1()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/count",
            payload={}
        )

        assert isinstance(response, ReviewCountV1Response)
        assert response.unprocessed == 8
