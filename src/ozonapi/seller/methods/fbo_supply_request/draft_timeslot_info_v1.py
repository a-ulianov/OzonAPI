from ...core import APIManager
from ...schemas.fbo_supply_request import (
    DraftTimeslotInfoV1Request,
    DraftTimeslotInfoV1Response,
)


class DraftTimeslotInfoV1Mixin(APIManager):
    """Реализует метод /v1/draft/timeslot/info"""

    async def draft_timeslot_info_v1(
            self: "DraftTimeslotInfoV1Mixin",
            request: DraftTimeslotInfoV1Request
    ) -> DraftTimeslotInfoV1Response:
        """Возвращает доступные таймслоты отгрузки для черновика заявки (версия 1).

        Notes:
            • Принимает `draft_id` и список складов (`warehouse_ids`). Предпочтительна
              версия `draft_timeslot_info()` (v2).
            • `date_from`/`date_to` — в формате `YYYY-MM-DD` (требование сервера).

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftTimeslotInfo

        Args:
            request: Запрос таймслотов по схеме `DraftTimeslotInfoV1Request`

        Returns:
            Доступные таймслоты по схеме `DraftTimeslotInfoV1Response`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.draft_timeslot_info_v1(
                    DraftTimeslotInfoV1Request(
                        draft_id=123456,
                        warehouse_ids=["1"],
                        date_from="2026-06-01",
                        date_to="2026-06-07"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="draft/timeslot/info",
            payload=request.model_dump(by_alias=True)
        )
        return DraftTimeslotInfoV1Response(**response)
