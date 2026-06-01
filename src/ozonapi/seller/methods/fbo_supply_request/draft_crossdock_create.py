from ...core import APIManager
from ...schemas.fbo_supply_request import DraftCrossdockCreateRequest
from ...schemas.fbo_supply_request.entities import DraftTypedCreateResponse


class DraftCrossdockCreateMixin(APIManager):
    """Реализует метод /v1/draft/crossdock/create"""

    async def draft_crossdock_create(
            self: "DraftCrossdockCreateMixin",
            request: DraftCrossdockCreateRequest
    ) -> DraftTypedCreateResponse:
        """Создаёт черновик заявки на поставку кросс-докингом.

        Notes:
            • Поставка через транзитный склад: товары одного кластера отгружаются в
              точку отгрузки (`delivery_info`). Возвращает `draft_id` и ошибки расчёта.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftCrossdockCreate

        Args:
            request: Запрос создания черновика по схеме `DraftCrossdockCreateRequest`

        Returns:
            Идентификатор черновика по схеме `DraftTypedCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_crossdock_create(
                    DraftCrossdockCreateRequest(
                        cluster_info=DraftTypedClusterInfo(
                            items=[DraftTypedItem(sku=123, quantity=10)],
                            macrolocal_cluster_id=1
                        ),
                        delivery_info=DraftTypedDeliveryInfo(
                            type=SupplyDeliveryType.DROPOFF
                        )
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/crossdock/create",
            payload=request.model_dump(by_alias=True)
        )
        return DraftTypedCreateResponse(**response)
