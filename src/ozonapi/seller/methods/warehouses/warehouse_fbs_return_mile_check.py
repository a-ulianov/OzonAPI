from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSReturnMileCheckRequest,
    WarehouseFBSReturnMileCheckResponse,
)


class WarehouseFBSReturnMileCheckMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/return-mile/check"""

    async def warehouse_fbs_return_mile_check(
            self: "WarehouseFBSReturnMileCheckMixin",
            request: WarehouseFBSReturnMileCheckRequest
    ) -> WarehouseFBSReturnMileCheckResponse:
        """Проверяет необходимость установки возвратной мили на склад FBS.

        Notes:
            • Если `should_set_return_mile` равно true, укажите пункт возврата
              при создании или обновлении склада.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsReturnMileCheck

        Args:
            request: Запрос по схеме `WarehouseFBSReturnMileCheckRequest`

        Returns:
            Результат проверки по схеме `WarehouseFBSReturnMileCheckResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_fbs_return_mile_check(
                    WarehouseFBSReturnMileCheckRequest(warehouse_id=123, country_code="RU")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/return-mile/check",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSReturnMileCheckResponse(**response)
