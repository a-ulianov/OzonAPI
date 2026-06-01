import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    CargoesRulesGetRequest,
    CargoesRulesGetResponse,
)


class TestCargoesRulesGet:
    """Тесты для метода cargoes_rules_get."""

    @pytest.mark.asyncio
    async def test_cargoes_rules_get(self, api, mock_api_request):
        """Тестирует метод cargoes_rules_get."""

        mock_api_request.return_value = {
            "supply_check_lists": [
                {
                    "supply_id": 123,
                    "cargoes_presents_rule": {
                        "cargo_count_per_type": [{"count": 1, "type": "BOX"}],
                        "count": 1,
                        "satisfied": True,
                    },
                    "edit_deadline_expire_rule": {
                        "is_applicable": True,
                        "is_required": False,
                        "satisfied": True,
                    },
                    "placement_zones_rule": {
                        "count_cargoes_all": 1,
                        "count_cargoes_with_mono_placement_zone": 1,
                        "is_applicable": True,
                        "satisfied": True,
                    },
                }
            ]
        }

        request = CargoesRulesGetRequest(supply_ids=["123"])

        response = await api.cargoes_rules_get(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cargoes/rules/get",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, CargoesRulesGetResponse)
        assert response.supply_check_lists[0].supply_id == 123
        assert response.supply_check_lists[0].cargoes_presents_rule.satisfied is True
