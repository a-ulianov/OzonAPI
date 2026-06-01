from ...core import APIManager
from ...schemas.fbo_supply_request import DraftMultiClusterCreateRequest
from ...schemas.fbo_supply_request.entities import DraftTypedCreateResponse


class DraftMultiClusterCreateMixin(APIManager):
    """Реализует метод /v1/draft/multi-cluster/create"""

    async def draft_multi_cluster_create(
            self: "DraftMultiClusterCreateMixin",
            request: DraftMultiClusterCreateRequest
    ) -> DraftTypedCreateResponse:
        """Создаёт черновик заявки на поставку для нескольких кластеров.

        Notes:
            • Товары распределяются по нескольким кластерам (`clusters_info`) с общей
              точкой отгрузки. Возвращает `draft_id` и ошибки расчёта.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftMultiClusterCreate

        Args:
            request: Запрос создания черновика по схеме `DraftMultiClusterCreateRequest`

        Returns:
            Идентификатор черновика по схеме `DraftTypedCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_multi_cluster_create(
                    DraftMultiClusterCreateRequest(
                        clusters_info=[
                            DraftTypedClusterInfo(
                                items=[DraftTypedItem(sku=123, quantity=10)],
                                macrolocal_cluster_id=1
                            )
                        ],
                        delivery_info=DraftTypedDeliveryInfo(
                            type=SupplyDeliveryType.DROPOFF
                        )
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/multi-cluster/create",
            payload=request.model_dump(by_alias=True)
        )
        return DraftTypedCreateResponse(**response)
