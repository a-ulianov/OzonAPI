from ...core import APIManager
from ...schemas.passes import (
    CarriagePassCreateRequest,
    CarriagePassCreateResponse,
)


class CarriagePassCreateMixin(APIManager):
    """Реализует метод /v1/carriage/pass/create"""

    async def carriage_pass_create(
            self: "CarriagePassCreateMixin",
            request: CarriagePassCreateRequest
    ) -> CarriagePassCreateResponse:
        """Создаёт пропуск на склад для перевозки FBS.

        Notes:
            • Пропуск оформляется на перевозку `carriage_id`; в одном запросе можно
              создать несколько пропусков.
            • Установите `with_returns`, если на этой машине будут вывозиться возвраты.

        References:
            https://docs.ozon.ru/api/seller/#operation/carriagePassCreate

        Args:
            request: Запрос на создание пропуска по схеме `CarriagePassCreateRequest`

        Returns:
            Идентификаторы созданных пропусков по схеме `CarriagePassCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_pass_create(
                    CarriagePassCreateRequest(
                        carriage_id=123,
                        arrival_passes=[{
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
            endpoint="carriage/pass/create",
            payload=request.model_dump()
        )
        return CarriagePassCreateResponse(**response)
