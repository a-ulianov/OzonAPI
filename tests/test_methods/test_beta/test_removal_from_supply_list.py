import pytest

from src.ozonapi.seller.schemas.beta import (
    RemovalFromSupplyListRequest,
    RemovalFromSupplyListResponse,
)


class TestRemovalFromSupplyList:
    """Тесты для метода removal_from_supply_list."""

    @pytest.mark.asyncio
    async def test_removal_from_supply_list(self, api, mock_api_request):
        """Тестирует метод removal_from_supply_list."""

        mock_api_request.return_value = {
            "last_id": "abc",
            "returns_summary_report_rows": [
                {"return_id": 5, "sku": 222, "offer_id": "art-1", "return_state": "DONE"}
            ],
        }

        request = RemovalFromSupplyListRequest(
            date_from="2026-05-01", date_to="2026-06-01", limit=100
        )

        response = await api.removal_from_supply_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="removal/from-supply/list",
            payload=request.model_dump()
        )

        assert isinstance(response, RemovalFromSupplyListResponse)
        assert response.last_id == "abc"
        assert response.returns_summary_report_rows[0].return_id == 5
