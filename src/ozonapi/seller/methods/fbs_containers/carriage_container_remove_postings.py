from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerRemovePostingsRequest,
    CarriageContainerRemovePostingsResponse,
)


class CarriageContainerRemovePostingsMixin(APIManager):
    """Реализует метод /v1/carriage/container/remove-postings"""

    async def carriage_container_remove_postings(
            self: "CarriageContainerRemovePostingsMixin",
            request: CarriageContainerRemovePostingsRequest
    ) -> CarriageContainerRemovePostingsResponse:
        """Метод для удаления отправлений из грузоместа.

        Notes:
            • Запускает асинхронную задачу; статус — `carriage_container_task_info()`.
            • В ответе возвращается `task_id` и ошибки по отправлениям, если они есть.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerRemovePostings

        Args:
            request: Запрос на удаление отправлений по схеме `CarriageContainerRemovePostingsRequest`

        Returns:
            Результат удаления отправлений по схеме `CarriageContainerRemovePostingsResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_remove_postings(
                    CarriageContainerRemovePostingsRequest(
                        container_id=12345,
                        posting_numbers=["33920113-1231-1"]
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/remove-postings",
            payload=request.model_dump()
        )
        return CarriageContainerRemovePostingsResponse(**response)
