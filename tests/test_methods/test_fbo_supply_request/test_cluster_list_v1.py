import pytest

from src.ozonapi.seller.common.enumerations.fbo_supply_request import SupplyClusterType
from src.ozonapi.seller.schemas.fbo_supply_request import (
    ClusterListV1Request,
    ClusterListV1Response,
)


class TestClusterListV1:
    """Тесты для метода cluster_list_v1 (устаревший v1)."""

    @pytest.mark.asyncio
    async def test_cluster_list_v1(self, api, mock_api_request):
        """Тестирует метод cluster_list_v1."""

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

        request = ClusterListV1Request(cluster_type=SupplyClusterType.OZON)

        response = await api.cluster_list_v1(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v1",
            endpoint="cluster/list",
            payload=request.model_dump(by_alias=True)
        )

        assert isinstance(response, ClusterListV1Response)
        assert response.clusters[0].id == 1
        assert response.clusters[0].logistic_clusters[0].warehouses[0].warehouse_id == 100
