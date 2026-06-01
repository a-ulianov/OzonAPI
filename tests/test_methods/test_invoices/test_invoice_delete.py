import pytest

from src.ozonapi.seller.schemas.invoices import (
    InvoiceDeleteRequest,
    InvoiceDeleteResponse,
)


class TestInvoiceDelete:
    """Тесты для метода invoice_delete."""

    @pytest.mark.asyncio
    async def test_invoice_delete(self, api, mock_api_request):
        """Тестирует метод invoice_delete."""

        mock_api_request.return_value = {"result": True}

        request = InvoiceDeleteRequest(posting_number="0001-1")

        response = await api.invoice_delete(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="invoice/delete",
            payload=request.model_dump()
        )

        assert isinstance(response, InvoiceDeleteResponse)
        assert response.result is True
