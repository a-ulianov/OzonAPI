import pytest

from src.ozonapi.seller.schemas.returns import ReturnsRfbsListRequest, ReturnsRfbsListResponse


class TestReturnsRfbsList:
    """Тесты для метода returns_rfbs_list."""

    @pytest.mark.asyncio
    async def test_returns_rfbs_list(self, api, mock_api_request):
        """Тестирует метод returns_rfbs_list."""

        mock_response_data = {
            "returns": [
                {
                    "return_id": 555,
                    "return_number": "RET-1",
                    "client_name": "Иван",
                    "order_number": "12345-0001",
                    "posting_number": "33920113-1231-1",
                    "product": {"name": "Товар", "sku": 987654, "price": 199, "currency_code": "RUB"},
                    "state": {"state": "ReturnStarted", "state_name": "Возврат начат"}
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReturnsRfbsListRequest(limit=100)

        response = await api.returns_rfbs_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="returns/rfbs/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsRfbsListResponse)
        assert response.returns[0].return_id == 555
        assert response.returns[0].product.sku == 987654
