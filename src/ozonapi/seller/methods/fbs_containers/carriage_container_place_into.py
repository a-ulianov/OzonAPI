from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerPlaceIntoRequest,
    CarriageContainerPlaceIntoResponse,
)


class CarriageContainerPlaceIntoMixin(APIManager):
    """Реализует метод /v1/carriage/container/place-into"""

    async def carriage_container_place_into(
            self: "CarriageContainerPlaceIntoMixin",
            request: CarriageContainerPlaceIntoRequest
    ) -> CarriageContainerPlaceIntoResponse:
        """Метод для размещения коробок на палете.

        Notes:
            • Помещает дочерние грузоместа (коробки) в родительское (палету).
            • Запускает асинхронную задачу; статус — `carriage_container_task_info()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerPlaceInto

        Args:
            request: Запрос на размещение коробок на палете по схеме `CarriageContainerPlaceIntoRequest`

        Returns:
            Результат размещения по схеме `CarriageContainerPlaceIntoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_place_into(
                    CarriageContainerPlaceIntoRequest(
                        parent_container_id=12345,
                        child_container_ids=["67890"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/place-into",
            payload=request.model_dump()
        )
        return CarriageContainerPlaceIntoResponse(**response)
