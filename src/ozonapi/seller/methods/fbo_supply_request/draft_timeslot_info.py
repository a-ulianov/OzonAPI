from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftTimeslotInfoRequest,
    DraftTimeslotInfoResponse,
)


class DraftTimeslotInfoMixin(APIManager):
    """Реализует метод /v2/draft/timeslot/info"""

    async def draft_timeslot_info(
            self: "DraftTimeslotInfoMixin",
            request: DraftTimeslotInfoRequest
    ) -> DraftTimeslotInfoResponse:
        """Возвращает доступные таймслоты отгрузки для черновика заявки.

        Notes:
            • Принимает `draft_id`, тип поставки и список кластеров/складов хранения.
              Таймслоты сгруппированы по датам в часовом поясе склада.
            • `date_from`/`date_to` — в формате `YYYY-MM-DD` (требование сервера).

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftTimeslotInfoV2

        Args:
            request: Запрос таймслотов по схеме `DraftTimeslotInfoRequest`

        Returns:
            Доступные таймслоты по схеме `DraftTimeslotInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_timeslot_info(
                    DraftTimeslotInfoRequest(
                        draft_id=123456,
                        supply_type=SupplyType.DIRECT,
                        date_from="2026-06-01",
                        date_to="2026-06-07",
                        selected_cluster_warehouses=[
                            DraftTimeslotInfoSelectedClusterWarehouse(
                                macrolocal_cluster_id=1, storage_warehouse_id=2
                            )
                        ]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v2",
            endpoint="draft/timeslot/info",
            payload=request.model_dump(by_alias=True)
        )
        return DraftTimeslotInfoResponse(**response)
