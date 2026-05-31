from ...core import APIManager
from ...schemas.returns import ReturnGiveoutListRequest, ReturnGiveoutListResponse


class ReturnGiveoutListMixin(APIManager):
    """Реализует метод /v1/return/giveout/list"""

    async def return_giveout_list(
            self: "ReturnGiveoutListMixin",
            request: ReturnGiveoutListRequest
    ) -> ReturnGiveoutListResponse:
        """Метод для получения списка возвратных отгрузок.

        Notes:
            • Возвращает список возвратных отгрузок с количеством товаров и складом.
            • Постраничный вывод через `limit` и `last_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/GiveoutAPI_GiveoutList

        Args:
            request: Запрос на получение списка отгрузок по схеме `ReturnGiveoutListRequest`

        Returns:
            Список возвратных отгрузок по схеме `ReturnGiveoutListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.return_giveout_list(
                    ReturnGiveoutListRequest(
                        limit=100
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="return/giveout/list",
            payload=request.model_dump()
        )
        return ReturnGiveoutListResponse(**response)
