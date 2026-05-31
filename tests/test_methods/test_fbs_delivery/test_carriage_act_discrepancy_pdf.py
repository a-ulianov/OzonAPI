import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    CarriageActDiscrepancyPDFRequest,
    CarriageActDiscrepancyPDFResponse,
)


class TestCarriageActDiscrepancyPDF:
    """Тесты для метода carriage_act_discrepancy_pdf."""

    @pytest.mark.asyncio
    async def test_carriage_act_discrepancy_pdf(self, api, mock_api_request):
        """Тестирует метод carriage_act_discrepancy_pdf."""

        mock_response_data = {
            "content": "JVBERi0xLjQK...",
            "name": "discrepancy.pdf",
            "type": "application/pdf"
        }
        mock_api_request.return_value = mock_response_data

        request = CarriageActDiscrepancyPDFRequest(carriage_id=12345)

        response = await api.carriage_act_discrepancy_pdf(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="carriage/act-discrepancy/pdf",
            payload=request.model_dump()
        )

        assert isinstance(response, CarriageActDiscrepancyPDFResponse)
        assert response.name == "discrepancy.pdf"
        assert response.content == "JVBERi0xLjQK..."
