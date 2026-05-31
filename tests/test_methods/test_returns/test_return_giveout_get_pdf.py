import pytest

from src.ozonapi.seller.schemas.returns import ReturnGiveoutGetPDFResponse


class TestReturnGiveoutGetPDF:
    """Тесты для метода return_giveout_get_pdf."""

    @pytest.mark.asyncio
    async def test_return_giveout_get_pdf(self, api, mock_api_request):
        """Тестирует метод return_giveout_get_pdf."""

        mock_api_request.return_value = {"pdf": "JVBERi0xLjQK..."}

        response = await api.return_giveout_get_pdf()

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="return/giveout/get-pdf",
            payload={}
        )

        assert isinstance(response, ReturnGiveoutGetPDFResponse)
        assert response.pdf == "JVBERi0xLjQK..."
