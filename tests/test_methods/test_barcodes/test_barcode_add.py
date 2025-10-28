import pytest

from src.ozonapi.seller.schemas.barcodes import (
    BarcodeAddRequest,
    BarcodeAddResponse,
)
from src.ozonapi.seller.schemas.barcodes.v1__barcode_add import BarcodeAddItem


class TestBarcodeAdd:
    """Тесты для метода barcode_add."""

    @pytest.mark.asyncio
    async def test_barcode_add(self, api, mock_api_request):
        """Тестирует метод barcode_add."""

        mock_response_data = {
            "errors": []
        }
        mock_api_request.return_value = mock_response_data

        request = BarcodeAddRequest(
            barcodes=[
                BarcodeAddItem(**{"sku": 123456, "barcode": "4321012345678"}),
                BarcodeAddItem(**{"sku": 789012, "barcode": "8765432101234"})
            ]
        )
        response = await api.barcode_add(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="barcode/add",
            payload=request.model_dump()
        )
        assert isinstance(response, BarcodeAddResponse)
        assert response.errors == []