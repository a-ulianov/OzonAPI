from ...core import APIManager
from ...schemas.fbo_supply_request import DraftDirectCreateRequest
from ...schemas.fbo_supply_request.entities import DraftTypedCreateResponse


class DraftDirectCreateMixin(APIManager):
    """Реализует метод /v1/draft/direct/create"""

    async def draft_direct_create(
            self: "DraftDirectCreateMixin",
            request: DraftDirectCreateRequest
    ) -> DraftTypedCreateResponse:
        """Создаёт черновик заявки на прямую поставку.

        Notes:
            • Прямая поставка на склад кластера без транзита. Возвращает `draft_id`
              и ошибки расчёта.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftDirectCreate

        Args:
            request: Запрос создания черновика по схеме `DraftDirectCreateRequest`

        Returns:
            Идентификатор черновика по схеме `DraftTypedCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_direct_create(
                    DraftDirectCreateRequest(
                        cluster_info=DraftTypedClusterInfo(
                            items=[DraftTypedItem(sku=123, quantity=10)],
                            macrolocal_cluster_id=1
                        )
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/direct/create",
            payload=request.model_dump(by_alias=True)
        )
        return DraftTypedCreateResponse(**response)
