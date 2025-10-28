import pytest

from src.ozonapi.seller.schemas.barcodes import (
    BarcodeGenerateRequest,
    BarcodeGenerateResponse,
)


class TestBarcodeGenerate:
    """Тесты для метода barcode_generate."""

    @pytest.mark.asyncio
    async def test_barcode_generate(self, api, mock_api_request):
        """Тестирует метод barcode_generate."""

        mock_response_data = {
            "errors": []
        }
        mock_api_request.return_value = mock_response_data

        request = BarcodeGenerateRequest(
            product_ids=[12345, 67890]
        )
        response = await api.barcode_generate(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="barcode/generate",
            payload=request.model_dump()
        )
        assert isinstance(response, BarcodeGenerateResponse)
        assert response.errors == []