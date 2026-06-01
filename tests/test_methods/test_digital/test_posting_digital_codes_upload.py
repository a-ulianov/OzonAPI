import pytest

from src.ozonapi.seller.schemas.digital import (
    PostingDigitalCodesUploadRequest,
    PostingDigitalCodesUploadResponse,
)


class TestPostingDigitalCodesUpload:
    """Тесты для метода posting_digital_codes_upload."""

    @pytest.mark.asyncio
    async def test_posting_digital_codes_upload(self, api, mock_api_request):
        """Тестирует метод posting_digital_codes_upload."""

        mock_api_request.return_value = {
            "exemplars_by_sku": [
                {
                    "sku": 123456,
                    "received_qty": 1,
                    "rejected_qty": 0,
                    "failed_exemplars": [],
                }
            ]
        }

        request = PostingDigitalCodesUploadRequest(
            posting_number="0001-1",
            exemplars_by_sku=[
                {
                    "sku": 123456,
                    "exemplar_qty": 1,
                    "not_available_exemplar_qty": 0,
                    "exemplar_keys": ["CODE-1"],
                }
            ],
        )

        response = await api.posting_digital_codes_upload(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/digital/codes/upload",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingDigitalCodesUploadResponse)
        assert response.exemplars_by_sku[0].sku == 123456
        assert response.exemplars_by_sku[0].received_qty == 1
