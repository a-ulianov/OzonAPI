import pytest

from src.ozonapi.seller.schemas.beta import SellerOzonLogisticsInfoResponse


class TestSellerOzonLogisticsInfo:
    """Тесты для метода seller_ozon_logistics_info."""

    @pytest.mark.asyncio
    async def test_seller_ozon_logistics_info(self, api, mock_api_request):
        """Тестирует метод seller_ozon_logistics_info."""
        mock_response_data = {
            "available_schemas": ["FBO", "FBS"],
            "ozon_logistics_enabled": True,
        }
        mock_api_request.return_value = mock_response_data

        response = await api.seller_ozon_logistics_info()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller/ozon-logistics/info",
            payload={},
        )
        assert isinstance(response, SellerOzonLogisticsInfoResponse)
        assert response.ozon_logistics_enabled is True
        assert response.available_schemas == ["FBO", "FBS"]
