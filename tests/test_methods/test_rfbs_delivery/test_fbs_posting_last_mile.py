import pytest

from src.ozonapi.seller.schemas.rfbs_delivery import (
    FbsPostingMoveStatusResponse,
    FbsPostingNumbersRequest,
)


class TestFbsPostingLastMile:
    """Тесты для метода fbs_posting_last_mile."""

    @pytest.mark.asyncio
    async def test_fbs_posting_last_mile(self, api, mock_api_request):
        """Тестирует метод fbs_posting_last_mile."""

        mock_api_request.return_value = {
            "result": [
                {"error": "", "posting_number": "123-456-1", "result": True}
            ]
        }

        request = FbsPostingNumbersRequest(posting_number=["123-456-1"])

        response = await api.fbs_posting_last_mile(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="fbs/posting/last-mile",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, FbsPostingMoveStatusResponse)
        assert response.result[0].result is True
