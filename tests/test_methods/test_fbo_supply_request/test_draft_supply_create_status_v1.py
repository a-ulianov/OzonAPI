import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftSupplyCreateStatusV1Request,
    DraftSupplyCreateStatusV1Response,
)


class TestDraftSupplyCreateStatusV1:
    """Тесты для метода draft_supply_create_status_v1."""

    @pytest.mark.asyncio
    async def test_draft_supply_create_status_v1(self, api, mock_api_request):
        """Тестирует метод draft_supply_create_status_v1."""

        mock_api_request.return_value = {
            "error_messages": [],
            "result": {"order_ids": ["7001", "7002"]},
            "status": "SUCCESS",
        }

        request = DraftSupplyCreateStatusV1Request(operation_id="op-123")

        response = await api.draft_supply_create_status_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/supply/create/status",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftSupplyCreateStatusV1Response)
        assert response.result.order_ids == ["7001", "7002"]
        assert response.status == "SUCCESS"
