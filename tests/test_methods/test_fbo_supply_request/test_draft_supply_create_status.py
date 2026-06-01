import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftSupplyCreateStatusRequest,
    DraftSupplyCreateStatusResponse,
)


class TestDraftSupplyCreateStatus:
    """Тесты для метода draft_supply_create_status."""

    @pytest.mark.asyncio
    async def test_draft_supply_create_status(self, api, mock_api_request):
        """Тестирует метод draft_supply_create_status."""

        mock_api_request.return_value = {
            "error_reasons": [],
            "order_id": 7001,
            "status": "SUCCESS",
        }

        request = DraftSupplyCreateStatusRequest(draft_id=123456)

        response = await api.draft_supply_create_status(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="draft/supply/create/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftSupplyCreateStatusResponse)
        assert response.order_id == 7001
        assert response.status == "SUCCESS"
