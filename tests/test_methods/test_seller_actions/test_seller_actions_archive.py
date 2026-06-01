import pytest

from src.ozonapi.seller.schemas.seller_actions import (
    SellerActionsArchiveRequest,
    SellerActionsArchiveResponse,
)


class TestSellerActionsArchive:
    """Тесты для метода seller_actions_archive."""

    @pytest.mark.asyncio
    async def test_seller_actions_archive(self, api, mock_api_request):
        """Тестирует метод seller_actions_archive."""

        mock_api_request.return_value = {}

        request = SellerActionsArchiveRequest(action_id=123456)

        response = await api.seller_actions_archive(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="seller-actions/archive",
            payload=request.model_dump(),
        )

        assert isinstance(response, SellerActionsArchiveResponse)
