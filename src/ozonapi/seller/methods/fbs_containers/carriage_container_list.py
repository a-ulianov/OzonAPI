from ...core import APIManager
from ...schemas.fbs_containers import (
    CarriageContainerListRequest,
    CarriageContainerListResponse,
)


class CarriageContainerListMixin(APIManager):
    """Реализует метод /v1/carriage/container/list"""

    async def carriage_container_list(
            self: "CarriageContainerListMixin",
            request: CarriageContainerListRequest
    ) -> CarriageContainerListResponse:
        """Метод для получения списка грузомест.

        Notes:
            • Возвращает грузоместа с фильтрацией по складу, типу, статусу и периоду создания.
            • Использует курсорную пагинацию: передавайте `cursor` из предыдущего ответа.
            • В фильтре необходимо передать `created_from` и `created_to`, а также указать
              `sort_dir` (`ASC`/`DESC`) — иначе API вернёт ошибку валидации.
            • Раздел beta: метод доступен для складов с поддержкой грузомест
              (сортируемый FBS); для прочих складов API возвращает `INVALID_ARGUMENT`.

        References:
            https://docs.ozon.ru/api/seller/#operation/CarriageAPI_CarriageContainerList

        Args:
            request: Запрос на получение списка грузомест по схеме `CarriageContainerListRequest`

        Returns:
            Список грузомест по схеме `CarriageContainerListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.carriage_container_list(
                    CarriageContainerListRequest(
                        filter=CarriageContainerListFilter(warehouse_id=12345),
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="carriage/container/list",
            payload=request.model_dump()
        )
        return CarriageContainerListResponse(**response)
