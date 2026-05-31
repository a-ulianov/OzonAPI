import pytest

from src.ozonapi.seller.schemas.returns import ReturnsRfbsGetRequest, ReturnsRfbsGetResponse


class TestReturnsRfbsGet:
    """Тесты для метода returns_rfbs_get."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_get(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_get."""

        mock_response_data = {
            "returns": {
                "return_number": "RET-1",
                "client_name": "Иван",
                "posting_number": "33920113-1231-1",
                "product": {"name": "Товар", "sku": 987654, "price": 199},
                "available_actions": [{"id": 1, "name": "approve"}],
                "return_reason": {"id": 5, "name": "Брак", "is_defect": True},
                "state": {"state": "ReturnStarted", "state_name": "Возврат начат"}
            }
        }
        mock_api_request.return_value = mock_response_data

        request = ReturnsRfbsGetRequest(return_id=12345)

        response = await api.returns_rfbs_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/get",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsGetResponse)
        assert response.returns.return_number == "RET-1"
        assert response.returns.available_actions[0].name == "approve"
        assert response.returns.return_reason.is_defect is True
