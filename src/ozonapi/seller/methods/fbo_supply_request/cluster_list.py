from ...core import APIManager
from ...schemas.fbo_supply_request import (
    ClusterListRequest,
    ClusterListResponse,
)


class ClusterListMixin(APIManager):
    """Реализует метод /v1/cluster/list"""

    async def cluster_list(
            self: "ClusterListMixin",
            request: ClusterListRequest
    ) -> ClusterListResponse:
        """Возвращает информацию о кластерах и их складах.

        Notes:
            • Кластеры нужны при создании черновика заявки на поставку FBO: по ним
              выбираются склады назначения. Можно отфильтровать по `cluster_ids`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftClusterList

        Args:
            request: Запрос информации о кластерах по схеме `ClusterListRequest`

        Returns:
            Информация о кластерах по схеме `ClusterListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cluster_list(
                    ClusterListRequest(cluster_type=SupplyClusterType.OZON)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cluster/list",
            payload=request.model_dump(by_alias=True)
        )
        return ClusterListResponse(**response)
