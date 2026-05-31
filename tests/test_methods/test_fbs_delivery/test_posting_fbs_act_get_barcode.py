import pytest

from src.ozonapi.seller.schemas.fbs_delivery import PostingFBSActGetBarcodeRequest, PostingFBSActGetBarcodeResponse


class TestPostingFBSActGetBarcode:
    """Тесты для метода posting_fbs_act_get_barcode."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_get_barcode(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_get_barcode."""

        mock_response_data = {"content": b"\x89PNG\r\n\x1a\n binary"}
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActGetBarcodeRequest(id=12345)

        response = await api.posting_fbs_act_get_barcode(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-barcode",
            payload=request.model_dump(),
            response_format="binary"
        )

        assert isinstance(response, PostingFBSActGetBarcodeResponse)
        assert response.content == b"\x89PNG\r\n\x1a\n binary"
