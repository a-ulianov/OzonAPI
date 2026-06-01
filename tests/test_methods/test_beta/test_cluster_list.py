import pytest

from src.ozonapi.seller.schemas.beta import ClusterListRequest, ClusterListResponse


class TestClusterList:
    """Тесты для метода cluster_list."""

    @pytest.mark.asyncio
    async def test_cluster_list(self, api, mock_api_request):
        """Тестирует метод cluster_list."""

        mock_api_request.return_value = {
            "result": [
                {
                    "macrolocal_cluster_id": 1,
                    "data": {
                        "fulfillments": [{"name": "Москва_РФЦ", "warehouse_id": 123}],
                        "macrolocal_cluster": {
                            "name": "Центр",
                            "country": {"name": "Россия", "uid": "RU"},
                        },
                    },
                }
            ]
        }

        request = ClusterListRequest()

        response = await api.cluster_list(request)

        mock_api_request.assert_called_once_with(
            method="post",
            api_version="v2",
            endpoint="cluster/list",
            payload=request.model_dump()
        )

        assert isinstance(response, ClusterListResponse)
        assert response.result[0].macrolocal_cluster_id == 1
        assert response.result[0].data.macrolocal_cluster.country.name == "Россия"
