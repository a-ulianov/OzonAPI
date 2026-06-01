from ...core import APIManager
from ...schemas.fbo_supply_request import WarehouseFboSellerListResponse


class WarehouseFboSellerListMixin(APIManager):
    """Реализует метод /v1/warehouse/fbo/seller/list"""

    async def warehouse_fbo_seller_list(
            self: "WarehouseFboSellerListMixin"
    ) -> WarehouseFboSellerListResponse:
        """Возвращает список складов продавца для прямых поставок FBO.

        Notes:
            • По каждому складу — адрес с координатами, контакты, рабочие дни,
              признаки активности и доступности отгрузки.

        References:
            https://docs.ozon.ru/api/seller/#operation/DraftAPI_WarehouseFboSellerList

        Returns:
            Список складов продавца по схеме `WarehouseFboSellerListResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbo_seller_list()
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbo/seller/list",
            payload={},
        )
        return WarehouseFboSellerListResponse(**response)
