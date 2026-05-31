from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerStatusGetRequest,
    CarriageContainerStatusGetResponse,
)


class CarriageContainerStatusGetMixin(APIManager):
    """Реализует метод /v1/carriage/container/status/get"""

    async def carriage_container_status_get(
            self: "CarriageContainerStatusGetMixin",
            request: CarriageContainerStatusGetRequest
    ) -> CarriageContainerStatusGetResponse:
        """Метод для получения статуса грузомест FBS.

        Notes:
            • Возвращает текущий статус для каждого переданного грузоместа.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerStatusGet

        Args:
            request: Запрос на получение статуса грузомест по схеме `CarriageContainerStatusGetRequest`

        Returns:
            Статусы грузомест по схеме `CarriageContainerStatusGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_status_get(
                    CarriageContainerStatusGetRequest(
                        container_ids=["12345"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/status/get",
            payload=request.model_dump()
        )
        return CarriageContainerStatusGetResponse(**response)
