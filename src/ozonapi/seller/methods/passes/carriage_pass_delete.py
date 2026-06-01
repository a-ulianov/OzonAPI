from ...core import APIManager
from ...schemas.passes import (
    CarriagePassDeleteRequest,
    CarriagePassDeleteResponse,
)


class CarriagePassDeleteMixin(APIManager):
    """Реализует метод /v1/carriage/pass/delete"""

    async def carriage_pass_delete(
            self: "CarriagePassDeleteMixin",
            request: CarriagePassDeleteRequest
    ) -> CarriagePassDeleteResponse:
        """Удаляет пропуска на склад для перевозки FBS.

        Notes:
            • Удаляет пропуска по их идентификаторам в рамках перевозки `carriage_id`.
            • Тело ответа отсутствует — успех подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/carriagePassDelete

        Args:
            request: Запрос на удаление пропусков по схеме `CarriagePassDeleteRequest`

        Returns:
            Пустой ответ по схеме `CarriagePassDeleteResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                await api.carriage_pass_delete(
                    CarriagePassDeleteRequest(
                        carriage_id=123, arrival_pass_ids=[456, 789]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/pass/delete",
            payload=request.model_dump()
        )
        return CarriagePassDeleteResponse(**response)
