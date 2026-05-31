from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerGetRequest,
    CarriageContainerGetResponse,
)


class CarriageContainerGetMixin(APIManager):
    """Реализует метод /v1/carriage/container/get"""

    async def carriage_container_get(
            self: "CarriageContainerGetMixin",
            request: CarriageContainerGetRequest
    ) -> CarriageContainerGetResponse:
        """Метод для получения информации о грузоместе.

        Notes:
            • Возвращает подробную информацию о грузоместе: статус, склад, отправления,
              товары, доступные действия и дочерние грузоместа.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerGet

        Args:
            request: Запрос на получение информации о грузоместе по схеме `CarriageContainerGetRequest`

        Returns:
            Информация о грузоместе по схеме `CarriageContainerGetResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_get(
                    CarriageContainerGetRequest(
                        container_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/get",
            payload=request.model_dump()
        )
        return CarriageContainerGetResponse(**response)
