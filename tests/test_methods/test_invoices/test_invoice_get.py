import pytest

from src.ozonapi.seller.schemas.invoices import (
    InvoiceGetRequest,
    InvoiceGetResponse,
)


class TestInvoiceGet:
    """Тесты для метода invoice_get."""

    @pytest.mark.asyncio
    async def test_invoice_get(self, api, mock_api_request):
        """Тестирует метод invoice_get."""

        mock_api_request.return_value = {
            "result": {
                "date": "2026-06-01T00:00:00Z",
                "file_url": "https://cdn.ozone.ru/invoice.pdf",
                "hs_codes": [{"code": "1234", "sku": "987654"}],
                "number": "INV-1",
                "price": 199.99,
                "price_currency": "USD",
            }
        }

        request = InvoiceGetRequest(posting_number="0001-1")

        response = await api.invoice_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="invoice/get",
            payload=request.model_dump()
        )

        assert isinstance(response, InvoiceGetResponse)
        assert response.result.number == "INV-1"
        assert response.result.hs_codes[0].sku == "987654"
        assert response.result.price == 199.99
