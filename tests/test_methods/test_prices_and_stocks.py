import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.methods import SellerPricesAndStocksAPI
from src.ozonapi.seller.schemas.prices_and_stocks import (
    ProductInfoPricesRequest,
    ProductInfoPricesResponse,
    ProductInfoStocksRequest,
    ProductInfoStocksResponse,
    ProductInfoStocksByWarehouseFBSRequest,
    ProductInfoStocksByWarehouseFBSResponse,
)


class TestSellerPricesAndStocksAPI:
    """Тесты для класса SellerPricesAndStocksAPI."""

    @pytest.fixture
    def seller_prices_stocks_api(self):
        """Фикстура для создания экземпляра SellerPricesAndStocksAPI."""
        return SellerPricesAndStocksAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerPricesAndStocksAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_product_info_prices(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_info_prices."""
        mock_response_data = {
            "items": [],
            "cursor": "test_cursor",
            "total": 0
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoPricesRequest()
        response = await seller_prices_stocks_api.product_info_prices(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v5",
            endpoint="product/info/prices",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoPricesResponse)
        assert response.cursor == "test_cursor"

    @pytest.mark.asyncio
    async def test_product_info_stocks(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_info_stocks."""
        mock_response_data = {
            "items": [],
            "cursor": "test_cursor",
            "total": 0
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoStocksRequest()
        response = await seller_prices_stocks_api.product_info_stocks(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v4",
            endpoint="product/info/stocks",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoStocksResponse)
        assert response.cursor == "test_cursor"

    @pytest.mark.asyncio
    async def test_product_info_stocks_by_warehouse_fbs(self, seller_prices_stocks_api, mock_api_manager_request):
        """Тестирует метод product_info_stocks_by_warehouse_fbs."""
        mock_response_data = {
            "result": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = ProductInfoStocksByWarehouseFBSRequest(
            sku=[9876543210]
        )
        response = await seller_prices_stocks_api.product_info_stocks_by_warehouse_fbs(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="product/info/stocks-by-warehouse/fbs",
            json=request.model_dump()
        )
        assert isinstance(response, ProductInfoStocksByWarehouseFBSResponse)
        assert response.result == []