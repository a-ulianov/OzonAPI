import pytest

from src.ozonapi.seller.schemas.cancellations import CancelReasonListResponse


class TestCancelReasonList:
    """Тесты для метода cancel_reason_list."""

    @pytest.mark.asyncio
    async def test_cancel_reason_list(self, api, mock_api_request):
        """Тестирует метод cancel_reason_list."""

        mock_api_request.return_value = {
            "reasons": [{"id": 352, "name": "Товар закончился"}]
        }

        response = await api.cancel_reason_list()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cancel-reason/list",
            payload={},
        )

        assert isinstance(response, CancelReasonListResponse)
        assert response.reasons[0].id == 352
        assert response.reasons[0].name == "Товар закончился"
