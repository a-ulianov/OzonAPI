from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerCreateRequest,
    CarriageContainerCreateResponse,
)


class CarriageContainerCreateMixin(APIManager):
    """Реализует метод /v1/carriage/container/create"""

    async def carriage_container_create(
            self: "CarriageContainerCreateMixin",
            request: CarriageContainerCreateRequest
    ) -> CarriageContainerCreateResponse:
        """Метод для создания грузоместа.

        Notes:
            • Создаёт указанное количество грузомест заданного типа на складе.
            • Метод раздела «Работа с грузоместами FBS» (beta).

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerCreate

        Args:
            request: Запрос на создание грузоместа по схеме `CarriageContainerCreateRequest`

        Returns:
            Идентификаторы созданных грузомест по схеме `CarriageContainerCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_create(
                    CarriageContainerCreateRequest(
                        cargo_type="box",
                        containers_count=1,
                        sort_type="sort",
                        warehouse_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/create",
            payload=request.model_dump()
        )
        return CarriageContainerCreateResponse(**response)
