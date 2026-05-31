from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerCancelRequest,
    CarriageContainerCancelResponse,
)


class CarriageContainerCancelMixin(APIManager):
    """Реализует метод /v1/carriage/container/cancel"""

    async def carriage_container_cancel(
            self: "CarriageContainerCancelMixin",
            request: CarriageContainerCancelRequest
    ) -> CarriageContainerCancelResponse:
        """Метод для отмены грузоместа.

        Notes:
            • Запускает асинхронную задачу отмены; статус — `carriage_container_task_info()`.
            • В ответе возвращается `task_id` и ошибки по грузоместам, если они есть.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerCancel

        Args:
            request: Запрос на отмену грузоместа по схеме `CarriageContainerCancelRequest`

        Returns:
            Результат отмены грузоместа по схеме `CarriageContainerCancelResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_cancel(
                    CarriageContainerCancelRequest(
                        container_ids=["12345"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/cancel",
            payload=request.model_dump()
        )
        return CarriageContainerCancelResponse(**response)
