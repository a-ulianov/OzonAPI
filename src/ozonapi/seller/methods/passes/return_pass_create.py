from ...core import APIManager
from ...schemas.passes import (
    ReturnPassCreateRequest,
    ReturnPassCreateResponse,
)


class ReturnPassCreateMixin(APIManager):
    """Реализует метод /v1/return/pass/create"""

    async def return_pass_create(
            self: "ReturnPassCreateMixin",
            request: ReturnPassCreateRequest
    ) -> ReturnPassCreateResponse:
        """Создаёт пропуск на склад для вывоза возвратов.

        Notes:
            • Пропуск начинает действовать с указанного времени `arrival_time` (UTC).
            • Идентификатор склада продавца `warehouse_id` можно получить методом
              `warehouse_list_v1()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/returnPassCreate

        Args:
            request: Запрос на создание пропуска для возврата по схеме
                `ReturnPassCreateRequest`

        Returns:
            Идентификаторы созданных пропусков по схеме `ReturnPassCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_pass_create(
                    ReturnPassCreateRequest(
                        arrival_passes=[{
                            "arrival_time": "2026-06-02T08:00:00Z",
                            "dropoff_point_id": 10,
                            "warehouse_id": 20,
                            "driver_name": "Иванов И.И.",
                            "driver_phone": "+79990000000",
                            "vehicle_license_plate": "А123БВ77",
                            "vehicle_model": "ГАЗель"
                        }]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/pass/create",
            payload=request.model_dump()
        )
        return ReturnPassCreateResponse(**response)
