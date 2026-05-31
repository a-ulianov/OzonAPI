import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutBarcodeResetResponse


class TestReturnGiveoutBarcodeReset:
    """Тесты для метода return_giveout_barcode_reset."""

    @pytest.mark.asyncio
    async def test_return_giveout_barcode_reset(self, api, mock_api_request):
        """Тестирует метод return_giveout_barcode_reset."""

        mock_api_request.return_value = {"png": "iVBORw0KGgo..."}

        response = await api.return_giveout_barcode_reset()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/barcode-reset",
            payload={}
        )

        assert isinstance(response, ReturnGiveoutBarcodeResetResponse)
        assert response.png == "iVBORw0KGgo..."
