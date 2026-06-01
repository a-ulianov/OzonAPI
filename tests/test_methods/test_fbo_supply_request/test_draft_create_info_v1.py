import pytest

from src.ozonapi.seller.schemas.fbo_supply_request import (
    DraftCreateInfoV1Request,
    DraftCreateInfoV1Response,
)


class TestDraftCreateInfoV1:
    """Тесты для метода draft_create_info_v1."""

    @pytest.mark.asyncio
    async def test_draft_create_info_v1(self, api, mock_api_request):
        """Тестирует метод draft_create_info_v1."""

        mock_api_request.return_value = {
            "clusters": [
                {
                    "cluster_id": 1,
                    "cluster_name": "Москва",
                    "warehouses": [
                        {
                            "bundle_ids": [{"bundle_id": "b-1", "is_docless": True}],
                            "status": {
                                "invalid_reason": "",
                                "is_available": True,
                                "state": "AVAILABLE",
                            },
                            "supply_warehouse": {
                                "address": "Москва",
                                "name": "Склад",
                                "warehouse_id": 100,
                            },
                            "total_rank": 1,
                            "total_score": 8.0,
                            "travel_time_days": 3,
                        }
                    ],
                }
            ],
            "draft_id": 555,
            "errors": [],
            "status": "CALCULATION_STATUS_SUCCESS",
        }

        request = DraftCreateInfoV1Request(operation_id="op-123")

        response = await api.draft_create_info_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="draft/create/info",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, DraftCreateInfoV1Response)
        assert response.draft_id == 555
        assert response.clusters[0].warehouses[0].bundle_ids[0].bundle_id == "b-1"
