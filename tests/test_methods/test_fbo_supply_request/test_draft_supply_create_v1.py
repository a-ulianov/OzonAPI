import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftSupplyCreateV1Request,
    DraftSupplyCreateV1Response,
)


class TestDraftSupplyCreateV1:
    """Тесты для метода draft_supply_create_v1."""

    @pytest.mark.asyncio
    async def test_draft_supply_create_v1(self, api, mock_api_request):
        """Тестирует метод draft_supply_create_v1."""

        mock_api_request.return_value = {"operation_id": "op-555"}

        request = DraftSupplyCreateV1Request(draft_id=123456, warehouse_id=100)

        response = await api.draft_supply_create_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/supply/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftSupplyCreateV1Response)
        assert response.operation_id == "op-555"
