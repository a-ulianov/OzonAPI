import pytest

from src.ozonapi.seller.schemas.rfbs_delivery import (
    FbsPostingMoveStatusResponse,
    FbsPostingTrackingNumber,
    FbsPostingTrackingNumberSetRequest,
)


class TestFbsPostingTrackingNumberSet:
    """Тесты для метода fbs_posting_tracking_number_set."""

    @pytest.mark.asyncio
    async def test_fbs_posting_tracking_number_set(self, api, mock_api_request):
        """Тестирует метод fbs_posting_tracking_number_set."""

        mock_api_request.return_value = {
            "result": [
                {"error": "", "posting_number": "123-456-1", "result": True}
            ]
        }

        request = FbsPostingTrackingNumberSetRequest(
            tracking_numbers=[
                FbsPostingTrackingNumber(
                    posting_number="123-456-1", tracking_number="TN1"
                )
            ]
        )

        response = await api.fbs_posting_tracking_number_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="fbs/posting/tracking-number/set",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FbsPostingMoveStatusResponse)
        assert response.result[0].result is True
