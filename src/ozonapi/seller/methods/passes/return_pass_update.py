from ...core import APIManager
from ...schemas.passes import (
    ReturnPassUpdateRequest,
    ReturnPassUpdateResponse,
)


class ReturnPassUpdateMixin(APIManager):
    """Реализует метод /v1/return/pass/update"""

    async def return_pass_update(
            self: "ReturnPassUpdateMixin",
            request: ReturnPassUpdateRequest
    ) -> ReturnPassUpdateResponse:
        """Обновляет пропуск на склад для вывоза возвратов.

        Notes:
            • Идентификатор обновляемого пропуска передаётся в поле `arrival_pass_id`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/returnPassUpdate

        Args:
            request: Запрос на обновление пропуска для возврата по схеме
                `ReturnPassUpdateRequest`

        Returns:
            Пустой ответ по схеме `ReturnPassUpdateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.return_pass_update(
                    ReturnPassUpdateRequest(
                        arrival_passes=[{
                            "arrival_pass_id": 456,
                            "arrival_time": "2026-06-02T08:00:00Z",
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
            endpoint="return/pass/update",
            payload=request.model_dump()
        )
        return ReturnPassUpdateResponse(**response)
