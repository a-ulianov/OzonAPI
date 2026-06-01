import pytest

from src.ozonapi.seller.schemas.invoices import (
    InvoiceFileUploadRequest,
    InvoiceFileUploadResponse,
)


class TestInvoiceFileUpload:
    """Тесты для метода invoice_file_upload."""

    @pytest.mark.asyncio
    async def test_invoice_file_upload(self, api, mock_api_request):
        """Тестирует метод invoice_file_upload."""

        mock_api_request.return_value = {"url": "https://cdn.ozone.ru/invoice.pdf"}

        request = InvoiceFileUploadRequest(
            base64_content="JVBERi0xLjQK",
            posting_number="0001-1",
        )

        response = await api.invoice_file_upload(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="invoice/file/upload",
            payload=request.model_dump()
        )

        assert isinstance(response, InvoiceFileUploadResponse)
        assert response.url == "https://cdn.ozone.ru/invoice.pdf"
