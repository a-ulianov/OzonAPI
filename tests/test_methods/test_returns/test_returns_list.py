import pytest

from src.ozonapi.seller.schemas.returns import ReturnsListRequest, ReturnsListResponse


class TestReturnsList:
    """Тесты для метода returns_list."""

    @pytest.mark.asyncio
    async def test_returns_list(self, api, mock_api_request):
        """Тестирует метод returns_list."""

        mock_response_data = {
            "has_next": True,
            "returns": [
                {
                    "id": 555,
                    "schema": "FBS",
                    "order_id": 999,
                    "order_number": "12345-0001",
                    "product": {
                        "sku": 987654,
                        "name": "Товар",
                        "price": {"price": 199.0, "currency_code": "RUB"},
                        "quantity": 1
                    },
                    "visual": {"status": {"id": 1, "sys_name": "DisputeOpened"}},
                    "exemplars": [{"id": 1}]
                }
            ]
        }
        mock_api_request.return_value = mock_response_data

        request = ReturnsListRequest(limit=100)

        response = await api.returns_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="returns/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ReturnsListResponse)
        assert response.returns[0].id == 555
        assert response.returns[0].schema_ == "FBS"
        assert response.returns[0].product.price.price == 199.0
