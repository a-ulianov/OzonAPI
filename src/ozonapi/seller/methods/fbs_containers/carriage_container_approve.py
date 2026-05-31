from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerApproveRequest,
    CarriageContainerApproveResponse,
)


class CarriageContainerApproveMixin(APIManager):
    """Реализует метод /v1/carriage/container/approve"""

    async def carriage_container_approve(
            self: "CarriageContainerApproveMixin",
            request: CarriageContainerApproveRequest
    ) -> CarriageContainerApproveResponse:
        """Метод для подтверждения состава грузоместа.

        Notes:
            • Запускает асинхронное подтверждение; статус — `carriage_container_task_info()`.
            • В ответе возвращается `task_id` и ошибки по грузоместам, если они есть.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerApprove

        Args:
            request: Запрос на подтверждение грузоместа по схеме `CarriageContainerApproveRequest`

        Returns:
            Результат подтверждения грузоместа по схеме `CarriageContainerApproveResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_approve(
                    CarriageContainerApproveRequest(
                        container_ids=["12345"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/approve",
            payload=request.model_dump()
        )
        return CarriageContainerApproveResponse(**response)
