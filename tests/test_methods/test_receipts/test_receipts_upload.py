import aiohttp
import pytest

from src.ozonapi.seller.schemas.receipts import (
    ReceiptsUploadRequest,
    ReceiptsUploadResponse,
)


class TestReceiptsUpload:
    """Тесты для метода receipts_upload."""

    @pytest.mark.asyncio
    async def test_receipts_upload(self, api, mock_api_request):
        """Тестирует метод receipts_upload (multipart/form-data)."""

        mock_api_request.return_value = {"receipt_id": "123"}

        request = ReceiptsUploadRequest(
            content=b"%PDF-1.4 receipt",
            operation_type="COMMODITY",
            posting_numbers=["0001-1", "0002-1"],
            receipt_number="RCPT-1",
            type="INCOMING",
        )

        response = await api.receipts_upload(request)

        mock_api_request.assert_called_once()
        kwargs = mock_api_request.call_args.kwargs
        assert kwargs["method"] == "post"
        assert kwargs["api_version"] == "v1"
        assert kwargs["endpoint"] == "receipts/upload"
        assert isinstance(kwargs["form_data"], aiohttp.FormData)

        assert isinstance(response, ReceiptsUploadResponse)
        assert response.receipt_id == "123"
