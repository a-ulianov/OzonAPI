import pytest

from src.ozonapi.seller.schemas.fbs_delivery import (
    PostingFBSActGetContainerLabelsRequest,
    PostingFBSActGetContainerLabelsResponse,
)


class TestPostingFBSActGetContainerLabels:
    """Тесты для метода posting_fbs_act_get_container_labels."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_get_container_labels(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_get_container_labels."""

        mock_response_data = {"content": b"%PDF-1.4 labels"}
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActGetContainerLabelsRequest(id=12345)

        response = await api.posting_fbs_act_get_container_labels(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/get-container-labels",
            payload=request.model_dump(),
            response_format="binary"
        )

        assert isinstance(response, PostingFBSActGetContainerLabelsResponse)
        assert response.content == b"%PDF-1.4 labels"
