from ...core import APIManager
from ...schemas.passes import (
    CarriagePassUpdateRequest,
    CarriagePassUpdateResponse,
)


class CarriagePassUpdateMixin(APIManager):
    """Реализует метод /v1/carriage/pass/update"""

    async def carriage_pass_update(
            self: "CarriagePassUpdateMixin",
            request: CarriagePassUpdateRequest
    ) -> CarriagePassUpdateResponse:
        """Обновляет пропуск на склад для перевозки FBS.

        Notes:
            • Идентификатор обновляемого пропуска передаётся в поле `id` элемента
              `arrival_passes`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/carriagePassUpdate

        Args:
            request: Запрос на обновление пропуска по схеме `CarriagePassUpdateRequest`

        Returns:
            Пустой ответ по схеме `CarriagePassUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.carriage_pass_update(
                    CarriagePassUpdateRequest(
                        carriage_id=123,
                        arrival_passes=[{
                            "id": 456,
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
            endpoint="carriage/pass/update",
            payload=request.model_dump()
        )
        return CarriagePassUpdateResponse(**response)
