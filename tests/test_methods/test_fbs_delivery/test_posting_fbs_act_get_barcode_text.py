import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSActGetBarcodeTextRequest,
    PostingFBSActGetBarcodeTextResponse,
)


class TestPostingFBSActGetBarcodeText:
    """Тесты для метода posting_fbs_act_get_barcode_text."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_get_barcode_text(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_get_barcode_text."""

        mock_response_data = {"result": "%0A0102%1D..."}
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActGetBarcodeTextRequest(id=12345)

        response = await api.posting_fbs_act_get_barcode_text(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-barcode/text",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSActGetBarcodeTextResponse)
        assert response.result == "%0A0102%1D..."
