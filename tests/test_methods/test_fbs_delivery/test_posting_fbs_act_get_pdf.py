import pytest

from src.ozonapi.seller.schemas.fbs_delivery import PostingFBSActGetPDFRequest, PostingFBSActGetPDFResponse


class TestPostingFBSActGetPDF:
    """Тесты для метода posting_fbs_act_get_pdf."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_get_pdf(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_get_pdf."""

        mock_response_data = {"content": b"%PDF-1.4 binary content"}
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActGetPDFRequest(id=12345)

        response = await api.posting_fbs_act_get_pdf(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-pdf",
            payload=request.model_dump(),
            response_format="binary"
        )

        assert isinstance(response, PostingFBSActGetPDFResponse)
        assert response.content == b"%PDF-1.4 binary content"
