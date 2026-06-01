from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftSupplyCreateRequest,
    DraftSupplyCreateResponse,
)


class DraftSupplyCreateMixin(APIManager):
    """Реализует метод /v2/draft/supply/create"""

    async def draft_supply_create(
            self: "DraftSupplyCreateMixin",
            request: DraftSupplyCreateRequest
    ) -> DraftSupplyCreateResponse:
        """Создаёт заявку на поставку по подтверждённому черновику.

        Notes:
            • Запускает асинхронное создание заявки; результат — через
              `draft_supply_create_status()` по `draft_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftSupplyCreateV2

        Args:
            request: Запрос создания заявки по схеме `DraftSupplyCreateRequest`

        Returns:
            Результат запуска создания по схеме `DraftSupplyCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_supply_create(
                    DraftSupplyCreateRequest(
                        draft_id=123456,
                        supply_type=SupplyType.DIRECT,
                        selected_cluster_warehouses=[
                            DraftSupplyCreateSelectedClusterWarehouse(
                                macrolocal_cluster_id=1, storage_warehouse_id=2
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="draft/supply/create",
            payload=request.model_dump(by_alias=True)
        )
        return DraftSupplyCreateResponse(**response)
