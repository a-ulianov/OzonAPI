import pytest

from src.ozonapi.seller.schemas.fbs_delivery import PostingFBSActCreateRequest, PostingFBSActCreateResponse


class TestPostingFBSActCreate:
    """Тесты для метода posting_fbs_act_create."""

    @pytest.mark.asyncio
    async def test_posting_fbs_act_create(self, api, mock_api_request):
        """Тестирует метод posting_fbs_act_create."""

        mock_response_data = {"result": {"id": 777}}
        mock_api_request.return_value = mock_response_data

        request = PostingFBSActCreateRequest(delivery_method_id=999, containers_count=2)

        response = await api.posting_fbs_act_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="posting/fbs/act/create",
            payload=request.model_dump()
        )

        assert isinstance(response, PostingFBSActCreateResponse)
        assert response.result.id == 777
