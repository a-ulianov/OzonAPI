from ...core import APIManager
from ...schemas.fbo_supply_request import (
    ClusterListV1Request,
    ClusterListV1Response,
)


class ClusterListV1Mixin(APIManager):
    """Реализует метод /v1/cluster/list"""

    async def cluster_list_v1(
            self: "ClusterListV1Mixin",
            request: ClusterListV1Request
    ) -> ClusterListV1Response:
        """Возвращает информацию о кластерах и их складах (API v1).

        Notes:
            • Устаревшая версия: используйте каноническую `cluster_list()` (v2).
            • Кластеры нужны при создании черновика заявки на поставку FBO: по ним
              выбираются склады назначения. Можно отфильтровать по `cluster_ids`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftClusterList

        Args:
            request: Запрос информации о кластерах по схеме `ClusterListV1Request`

        Returns:
            Информация о кластерах по схеме `ClusterListV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cluster_list_v1(
                    ClusterListV1Request(cluster_type=SupplyClusterType.OZON)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cluster/list",
            payload=request.model_dump(by_alias=True)
        )
        return ClusterListV1Response(**response)
