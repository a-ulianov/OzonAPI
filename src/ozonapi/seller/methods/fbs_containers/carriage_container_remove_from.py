from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerRemoveFromRequest,
    CarriageContainerRemoveFromResponse,
)


class CarriageContainerRemoveFromMixin(APIManager):
    """Реализует метод /v1/carriage/container/remove-from"""

    async def carriage_container_remove_from(
            self: "CarriageContainerRemoveFromMixin",
            request: CarriageContainerRemoveFromRequest
    ) -> CarriageContainerRemoveFromResponse:
        """Метод для удаления коробок с палеты.

        Notes:
            • Убирает дочерние грузоместа (коробки) из родительского (палеты).
            • Запускает асинхронную задачу; статус — `carriage_container_task_info()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerRemoveFrom

        Args:
            request: Запрос на удаление коробок с палеты по схеме `CarriageContainerRemoveFromRequest`

        Returns:
            Результат удаления по схеме `CarriageContainerRemoveFromResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_remove_from(
                    CarriageContainerRemoveFromRequest(
                        parent_container_id=12345,
                        child_container_ids=["67890"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/remove-from",
            payload=request.model_dump()
        )
        return CarriageContainerRemoveFromResponse(**response)
