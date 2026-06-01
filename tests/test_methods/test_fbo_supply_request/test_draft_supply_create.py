import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftSupplyCreateRequest,
    DraftSupplyCreateResponse,
    DraftSupplyCreateSelectedClusterWarehouse,
    DraftSupplyCreateTimeslot,
)


class TestDraftSupplyCreate:
    """Тесты для метода draft_supply_create."""

    @pytest.mark.asyncio
    async def test_draft_supply_create(self, api, mock_api_request):
        """Тестирует метод draft_supply_create."""

        mock_api_request.return_value = {"draft_id": 123456, "error_reasons": []}

        request = DraftSupplyCreateRequest(
            draft_id=123456,
            supply_type=SupplyType.DIRECT,
            timeslot=DraftSupplyCreateTimeslot(
                from_in_timezone="2026-06-02T09:00:00+03:00",
                to_in_timezone="2026-06-02T12:00:00+03:00",
            ),
            selected_cluster_warehouses=[
                DraftSupplyCreateSelectedClusterWarehouse(
                    macrolocal_cluster_id=1, storage_warehouse_id=2
                )
            ],
        )

        response = await api.draft_supply_create(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="draft/supply/create",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftSupplyCreateResponse)
        assert response.draft_id == 123456
