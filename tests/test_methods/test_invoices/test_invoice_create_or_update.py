import pytest

from src.ozonapi.seller.schemas.invoices import (
    InvoiceCreateOrUpdateRequest,
    InvoiceCreateOrUpdateResponse,
)


class TestInvoiceCreateOrUpdate:
    """Тесты для метода invoice_create_or_update."""

    @pytest.mark.asyncio
    async def test_invoice_create_or_update(self, api, mock_api_request):
        """Тестирует метод invoice_create_or_update."""

        mock_api_request.return_value = {"result": True}

        request = InvoiceCreateOrUpdateRequest(
            date="2026-06-01T00:00:00Z",
            posting_number="0001-1",
            url="https://cdn.ozone.ru/invoice.pdf",
            number="INV-1",
            price=199.99,
            price_currency="USD",
            hs_codes=[{"code": "1234", "sku": "987654"}],
        )

        response = await api.invoice_create_or_update(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="invoice/create-or-update",
            payload=request.model_dump()
        )

        assert isinstance(response, InvoiceCreateOrUpdateResponse)
        assert response.result is True
        assert request.hs_codes[0].code == "1234"
