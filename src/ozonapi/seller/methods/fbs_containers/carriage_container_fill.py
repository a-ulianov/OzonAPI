from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerFillRequest,
    CarriageContainerFillResponse,
)


class CarriageContainerFillMixin(APIManager):
    """Реализует метод /v1/carriage/container/fill"""

    async def carriage_container_fill(
            self: "CarriageContainerFillMixin",
            request: CarriageContainerFillRequest
    ) -> CarriageContainerFillResponse:
        """Метод для наполнения грузоместа отправлениями.

        Notes:
            • Запускает асинхронное наполнение грузоместа; статус — `carriage_container_task_info()`.
            • В ответе возвращается `task_id` и ошибки по отправлениям, если они есть.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerFill

        Args:
            request: Запрос на наполнение грузоместа по схеме `CarriageContainerFillRequest`

        Returns:
            Результат наполнения грузоместа по схеме `CarriageContainerFillResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_fill(
                    CarriageContainerFillRequest(
                        container_id=12345,
                        posting_numbers=["33920113-1231-1"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/fill",
            payload=request.model_dump()
        )
        return CarriageContainerFillResponse(**response)
