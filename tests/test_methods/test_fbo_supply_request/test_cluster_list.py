import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyClusterType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    ClusterListRequest,
    ClusterListResponse,
)


class TestClusterList:
    """Тесты для метода cluster_list."""

    @pytest.mark.asyncio
    async def test_cluster_list(self, api, mock_api_request):
        """Тестирует метод cluster_list."""

        mock_api_request.return_value = {
            "clusters": [
                {
                    "id": 1,
                    "name": "Москва",
                    "type": "CLUSTER_TYPE_OZON",
                    "macrolocal_cluster_id": 10,
                    "logistic_clusters": [
                        {
                            "warehouses": [
                                {
                                    "name": "Склад",
                                    "type": "FULL_FILLMENT",
                                    "warehouse_id": 100,
                                }
                            ]
                        }
                    ],
                }
            ]
        }

        request = ClusterListRequest(cluster_type=SupplyClusterType.OZON)

        response = await api.cluster_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cluster/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ClusterListResponse)
        assert response.clusters[0].id == 1
        assert response.clusters[0].logistic_clusters[0].warehouses[0].warehouse_id == 100
