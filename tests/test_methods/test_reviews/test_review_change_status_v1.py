import pytest

from src.ozonapi.seller.schemas.reviews import (
    ReviewChangeStatusV1Request,
    ReviewChangeStatusV1Response,
)


class TestReviewChangeStatusV1:
    """Тесты для метода review_change_status_v1."""

    @pytest.mark.asyncio
    async def test_review_change_status_v1(self, api, mock_api_request):
        """Тестирует метод review_change_status_v1."""

        mock_api_request.return_value = {}

        request = ReviewChangeStatusV1Request(review_ids=["r-1"], status="PROCESSED")

        response = await api.review_change_status_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="review/change-status",
            payload=request.model_dump()
        )

        assert isinstance(response, ReviewChangeStatusV1Response)
