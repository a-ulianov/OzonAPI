from ...core import APIManager
from ...schemas.fbs_delivery import CarriageApproveRequest, CarriageApproveResponse


class CarriageApproveMixin(APIManager):
    """Реализует метод /v1/carriage/approve"""

    async def carriage_approve(
            self: "CarriageApproveMixin",
            request: CarriageApproveRequest
    ) -> CarriageApproveResponse:
        """Метод для подтверждения отгрузки.

        Notes:
            • Подтверждает отгрузку и фиксирует её состав.
            • Если вы подключены к схеме с грузовыми местами, передайте `containers_count`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageApprove

        Args:
            request: Запрос на подтверждение отгрузки по схеме `CarriageApproveRequest`

        Returns:
            Результат подтверждения отгрузки по схеме `CarriageApproveResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_approve(
                    CarriageApproveRequest(
                        carriage_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/approve",
            payload=request.model_dump()
        )
        return CarriageApproveResponse(**response)
