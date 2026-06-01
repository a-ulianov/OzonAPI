from ...core import APIManager
from ...schemas.beta import ClusterListRequest, ClusterListResponse


class ClusterListMixin(APIManager):
    """Реализует метод /v2/cluster/list"""

    async def cluster_list(
            self: "ClusterListMixin",
            request: ClusterListRequest
    ) -> ClusterListResponse:
        """Возвращает информацию о макролокальных кластерах.

        Notes:
            • Запрос без параметров.
            • Идентификаторы кластеров используются в методе `analytics_stocks()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftClusterList

        Args:
            request: Запрос по схеме `ClusterListRequest`

        Returns:
            Список кластеров по схеме `ClusterListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cluster_list(ClusterListRequest())
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="cluster/list",
            payload=request.model_dump()
        )
        return ClusterListResponse(**response)
