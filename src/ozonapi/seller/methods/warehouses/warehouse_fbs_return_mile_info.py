from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSReturnMileInfoRequest,
    WarehouseFBSReturnMileInfoResponse,
)


class WarehouseFBSReturnMileInfoMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/return-mile/info"""

    async def warehouse_fbs_return_mile_info(
            self: "WarehouseFBSReturnMileInfoMixin",
            request: WarehouseFBSReturnMileInfoRequest
    ) -> WarehouseFBSReturnMileInfoResponse:
        """Возвращает информацию о возвратной миле складов FBS.

        Notes:
            • Необходимость установки возвратной мили проверяется методом
              `warehouse_fbs_return_mile_check()`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFBSReturnMileInfo

        Args:
            request: Запрос по схеме `WarehouseFBSReturnMileInfoRequest`

        Returns:
            Настройки возвратной мили по схеме `WarehouseFBSReturnMileInfoResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_return_mile_info(
                    WarehouseFBSReturnMileInfoRequest(warehouse_ids=["123"])
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/return-mile/info",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSReturnMileInfoResponse(**response)
