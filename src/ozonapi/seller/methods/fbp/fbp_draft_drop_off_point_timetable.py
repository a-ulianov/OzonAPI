from ...core import APIManager
from ...schemas.fbp import (
    FbpDraftDropOffPointTimetableRequest,
    FbpDraftDropOffPointTimetableResponse,
)


class FbpDraftDropOffPointTimetableMixin(APIManager):
    """Реализует метод /v1/fbp/draft/drop-off/point/timetable"""

    async def fbp_draft_drop_off_point_timetable(
            self: "FbpDraftDropOffPointTimetableMixin",
            request: FbpDraftDropOffPointTimetableRequest,
    ) -> FbpDraftDropOffPointTimetableResponse:
        """Получает расписание работы drop-off пункта.

        Notes:
            • Возвращает расписание по дням недели с часами работы и перерыва.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpDraftDropOffPointTimetable

        Args:
            request: Параметры запроса по схеме `FbpDraftDropOffPointTimetableRequest`

        Returns:
            Расписание по схеме `FbpDraftDropOffPointTimetableResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_draft_drop_off_point_timetable(
                    FbpDraftDropOffPointTimetableRequest(
                        warehouse_id=123,
                        province_uuid="uuid-1",
                        drop_off_point_id=7,
                    )
                )

            for day in result.calendar:
                print(day.day_of_week, day.calendar_item)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/draft/drop-off/point/timetable",
            payload=request.model_dump(),
        )
        return FbpDraftDropOffPointTimetableResponse(**response)
