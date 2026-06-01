import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftCreateInfoRequest,
    DraftCreateInfoResponse,
)


class TestDraftCreateInfo:
    """Тесты для метода draft_create_info."""

    @pytest.mark.asyncio
    async def test_draft_create_info(self, api, mock_api_request):
        """Тестирует метод draft_create_info."""

        mock_api_request.return_value = {
            "clusters": [
                {
                    "cluster_name": "Москва",
                    "macrolocal_cluster_id": 10,
                    "supply_type": "DIRECT",
                    "warehouses": [
                        {
                            "availability_status": {
                                "invalid_reason": "",
                                "state": "AVAILABLE",
                            },
                            "bundle_id": "b-1",
                            "storage_warehouse": {
                                "address": "Москва",
                                "name": "Склад",
                                "warehouse_id": 100,
                            },
                            "supply_tags": ["TAG"],
                            "total_rank": 1,
                            "total_score": 9.5,
                        }
                    ],
                }
            ],
            "errors": [],
            "status": "CALCULATION_STATUS_SUCCESS",
        }

        request = DraftCreateInfoRequest(draft_id=123456)

        response = await api.draft_create_info(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="draft/create/info",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftCreateInfoResponse)
        assert response.clusters[0].supply_type == "DIRECT"
        assert response.clusters[0].warehouses[0].storage_warehouse.warehouse_id == 100
