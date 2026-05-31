import pytest

from src.ozonapi.seller.schemas.reviews import ReviewChangeStatusRequest, ReviewChangeStatusResponse


class TestReviewChangeStatus:
    """Тесты для метода review_change_status."""

    @pytest.mark.asyncio
    async def test_review_change_status(self, api, mock_api_request):
        """Тестирует метод review_change_status."""

        mock_api_request.return_value = {}

        request = ReviewChangeStatusRequest(review_ids=["r-1"], status="PROCESSED")

        response = await api.review_change_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="review/change-status",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewChangeStatusResponse)
