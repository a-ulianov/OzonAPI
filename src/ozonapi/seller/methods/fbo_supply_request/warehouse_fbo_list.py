from ...core import APIManager
from ...schemas.fbo_supply_request import (
    WarehouseFboListRequest,
    WarehouseFboListResponse,
)


class WarehouseFboListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbo/list"""

    async def warehouse_fbo_list(
            self: "WarehouseFboListMixin",
            request: WarehouseFboListRequest
    ) -> WarehouseFboListResponse:
        """Ищет точки отгрузки поставки FBO по названию.

        Notes:
            • Используется при создании черновика заявки на поставку: возвращает склады,
              пункты выдачи и сортировочные центры, доступные для отгрузки.
            • Фильтр по типу поставки (`filter_by_supply_type`) и поиск по названию.
            • `search` должен содержать не менее 4 символов (требование сервера).

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_DraftGetWarehouseFboList

        Args:
            request: Запрос поиска точек отгрузки по схеме `WarehouseFboListRequest`

        Returns:
            Результат поиска складов по схеме `WarehouseFboListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbo_list(
                    WarehouseFboListRequest(
                        filter_by_supply_type=[SupplyCreateType.DIRECT],
                        search="Москва"
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbo/list",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFboListResponse(**response)
