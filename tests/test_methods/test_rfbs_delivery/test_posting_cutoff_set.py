import pytest

from src.ozonapi.seller.schemas.rfbs_delivery import (
    PostingCutoffSetRequest,
    PostingCutoffSetResponse,
)


class TestPostingCutoffSet:
    """Тесты для метода posting_cutoff_set."""

    @pytest.mark.asyncio
    async def test_posting_cutoff_set(self, api, mock_api_request):
        """Тестирует метод posting_cutoff_set."""

        mock_api_request.return_value = {"result": True}

        request = PostingCutoffSetRequest(
            posting_number="123-456-1",
            new_cutoff_date="2026-06-02T00:00:00Z",
        )

        response = await api.posting_cutoff_set(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="posting/cutoff/set",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, PostingCutoffSetResponse)
        assert response.result is True
