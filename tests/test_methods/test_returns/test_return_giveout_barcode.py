import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutBarcodeResponse


class TestReturnGiveoutBarcode:
    """Тесты для метода return_giveout_barcode."""

    @pytest.mark.asyncio
    async def test_return_giveout_barcode(self, api, mock_api_request):
        """Тестирует метод return_giveout_barcode."""

        mock_api_request.return_value = {"barcode": "%0A0102%1D"}

        response = await api.return_giveout_barcode()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/barcode",
            payload={}
        )

        assert isinstance(response, ReturnGiveoutBarcodeResponse)
        assert response.barcode == "%0A0102%1D"
