from ...core import APIManager
from ...schemas.fbs_delivery import CarriageEttnStatusRequest, CarriageEttnStatusResponse


class CarriageEttnStatusMixin(APIManager):
    """Реализует метод /v1/carriage/ettn/status"""

    async def carriage_ettn_status(
            self: "CarriageEttnStatusMixin",
            request: CarriageEttnStatusRequest
    ) -> CarriageEttnStatusResponse:
        """Метод для получения статуса проверки электронной ТТН на прослеживаемой перевозке FBS.

        Notes:
            • Возвращает статус проверки электронной транспортной накладной (ЭТТН)
              для перевозки с прослеживаемыми товарами и список ошибок проверки.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageEttnStatus

        Args:
            request: Запрос на получение статуса проверки ЭТТН по схеме `CarriageEttnStatusRequest`

        Returns:
            Статус проверки ЭТТН по схеме `CarriageEttnStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_ettn_status(
                    CarriageEttnStatusRequest(
                        carriage_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/ettn/status",
            payload=request.model_dump()
        )
        return CarriageEttnStatusResponse(**response)
