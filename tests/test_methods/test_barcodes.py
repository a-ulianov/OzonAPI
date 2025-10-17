import pytest
from unittest.mock import AsyncMock, patch

from src.ozonapi.seller.methods import SellerBarcodeAPI
from src.ozonapi.seller.schemas.barcodes import (
    BarcodeAddRequest,
    BarcodeAddResponse,
    BarcodeGenerateRequest,
    BarcodeGenerateResponse,
)
from src.ozonapi.seller.schemas.barcodes.v1__barcode_add import BarcodeAddItem


class TestSellerBarcodeAPI:
    """Тесты для класса SellerBarcodeAPI."""

    @pytest.fixture
    def seller_barcode_api(self):
        """Фикстура для создания экземпляра SellerBarcodeAPI."""
        return SellerBarcodeAPI(client_id="test_client", api_key="test_api_key")

    @pytest.fixture
    def mock_api_manager_request(self):
        """Фикстура для мока метода _request APIManager."""
        with patch.object(SellerBarcodeAPI, '_request', new_callable=AsyncMock) as mock_request:
            yield mock_request

    @pytest.mark.asyncio
    async def test_barcode_add(self, seller_barcode_api, mock_api_manager_request):
        """Тестирует метод barcode_add."""

        mock_response_data = {
            "errors": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = BarcodeAddRequest(
            barcodes=[
                BarcodeAddItem(**{"sku": 123456, "barcode": "4321012345678"}),
                BarcodeAddItem(**{"sku": 789012, "barcode": "8765432101234"})
            ]
        )
        response = await seller_barcode_api.barcode_add(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="barcode/add",
            json=request.model_dump()
        )
        assert isinstance(response, BarcodeAddResponse)
        assert response.errors == []

    @pytest.mark.asyncio
    async def test_barcode_generate(self, seller_barcode_api, mock_api_manager_request):
        """Тестирует метод barcode_generate."""

        mock_response_data = {
            "errors": []
        }
        mock_api_manager_request.return_value = mock_response_data

        request = BarcodeGenerateRequest(
            product_ids=[12345, 67890]
        )
        response = await seller_barcode_api.barcode_generate(request)

        mock_api_manager_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="barcode/generate",
            json=request.model_dump()
        )
        assert isinstance(response, BarcodeGenerateResponse)
        assert response.errors == []