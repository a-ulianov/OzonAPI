from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerTaskInfoRequest,
    CarriageContainerTaskInfoResponse,
)


class CarriageContainerTaskInfoMixin(APIManager):
    """Реализует метод /v1/carriage/container/task/info"""

    async def carriage_container_task_info(
            self: "CarriageContainerTaskInfoMixin",
            request: CarriageContainerTaskInfoRequest
    ) -> CarriageContainerTaskInfoResponse:
        """Метод для получения статуса задачи грузового места.

        Notes:
            • Возвращает статус выполнения асинхронной задачи (наполнение, подтверждение,
              отмена и т.д.) по `task_id` из ответа соответствующего метода.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerTaskInfo

        Args:
            request: Запрос на получение статуса задачи по схеме `CarriageContainerTaskInfoRequest`

        Returns:
            Статус задачи по схеме `CarriageContainerTaskInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_task_info(
                    CarriageContainerTaskInfoRequest(
                        task_id=12345
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/task/info",
            payload=request.model_dump()
        )
        return CarriageContainerTaskInfoResponse(**response)
