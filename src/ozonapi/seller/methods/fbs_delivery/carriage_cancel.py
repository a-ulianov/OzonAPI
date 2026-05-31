from ...core import APIManager
from ...schemas.fbs_delivery import CarriageCancelRequest, CarriageCancelResponse


class CarriageCancelMixin(APIManager):
    """Реализует метод /v1/carriage/cancel"""

    async def carriage_cancel(
            self: "CarriageCancelMixin",
            request: CarriageCancelRequest
    ) -> CarriageCancelResponse:
        """Метод для удаления отгрузки.

        Notes:
            • Удаляет отгрузку, если её ещё можно отменить.
            • При невозможности удаления в поле `error` вернётся описание ошибки.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageCancel

        Args:
            request: Запрос на удаление отгрузки по схеме `CarriageCancelRequest`

        Returns:
            Результат удаления отгрузки по схеме `CarriageCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_cancel(
                    CarriageCancelRequest(
                        carriage_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/cancel",
            payload=request.model_dump()
        )
        return CarriageCancelResponse(**response)
