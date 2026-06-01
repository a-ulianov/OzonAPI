from ...core import APIManager
from ...schemas.fbp import (
    FbpOrderDropOffTimetableRequest,
    FbpOrderDropOffTimetableResponse,
)


class FbpOrderDropOffTimetableMixin(APIManager):
    """Реализует метод /v1/fbp/order/drop-off/timetable"""

    async def fbp_order_drop_off_timetable(
            self: "FbpOrderDropOffTimetableMixin",
            request: FbpOrderDropOffTimetableRequest,
    ) -> FbpOrderDropOffTimetableResponse:
        """Получает график работы drop-off пункта для поставки.

        Notes:
            • Возвращает расписание по дням недели с часами работы и перерыва.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPSupply_FbpOrderDropOffTimetable

        Args:
            request: Параметры запроса по схеме `FbpOrderDropOffTimetableRequest`

        Returns:
            Расписание по схеме `FbpOrderDropOffTimetableResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_order_drop_off_timetable(
                    FbpOrderDropOffTimetableRequest(
                        warehouse_id=123,
                        province_uuid="uuid-1",
                        drop_off_point_id=7,
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/order/drop-off/timetable",
            payload=request.model_dump(),
        )
        return FbpOrderDropOffTimetableResponse(**response)
