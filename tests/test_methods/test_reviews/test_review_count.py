import pytest

from src.ozonapi.seller.schemas.reviews import ReviewCountResponse


class TestReviewCount:
    """Тесты для метода review_count."""

    @pytest.mark.asyncio
    async def test_review_count(self, api, mock_api_request):
        """Тестирует метод review_count."""

        mock_api_request.return_value = {"total": 10, "new": 3, "viewed": 5, "processed": 2}

        response = await api.review_count()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="review/count",
            payload={}
        )

        assert isinstance(response, ReviewCountResponse)
        assert response.total == 10
        assert response.new == 3
