import pytest

from src.ozonapi.seller.schemas.cancellations import (
    CancelReasonListByPostingRequest,
    CancelReasonListByPostingResponse,
)


class TestCancelReasonListByPosting:
    """Тесты для метода cancel_reason_list_by_posting."""

    @pytest.mark.asyncio
    async def test_cancel_reason_list_by_posting(self, api, mock_api_request):
        """Тестирует метод cancel_reason_list_by_posting."""

        mock_api_request.return_value = {
            "reasons": [{"id": 352, "name": "Товар закончился"}]
        }

        request = CancelReasonListByPostingRequest(
            posting_number="0001-1234567-0000001"
        )

        response = await api.cancel_reason_list_by_posting(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cancel-reason/list-by-posting",
            payload=request.model_dump(),
        )

        assert isinstance(response, CancelReasonListByPostingResponse)
        assert response.reasons[0].name == "Товар закончился"
