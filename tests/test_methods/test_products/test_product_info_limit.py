import pytest

from src.ozonapi.seller.schemas.products import ProductInfoLimitResponse


class TestProductInfoLimit:
    """Тесты для метода product_info_limit."""

    @pytest.mark.asyncio
    async def test_product_info_limit(self, api, mock_api_request):
        """Тестирует метод product_info_limit."""
        mock_response_data = {
            "daily_create": {
                "limit": 1000,
                "reset_at": "2024-01-01T00:00:00Z",
                "usage": 150
            },
            "daily_update": {
                "limit": 2000,
                "reset_at": "2024-01-01T00:00:00Z",
                "usage": 300
            },
            "total": {
                "limit": 10000,
                "usage": 2500
            }
        }
        mock_api_request.return_value = mock_response_data

        response = await api.product_info_limit()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/limit",
            json={}
        )
        assert isinstance(response, ProductInfoLimitResponse)
        assert response.daily_create.limit == 1000
        assert response.daily_create.usage == 150
        assert response.daily_update.limit == 2000
        assert response.daily_update.usage == 300
        assert response.total.limit == 10000
        assert response.total.usage == 2500
