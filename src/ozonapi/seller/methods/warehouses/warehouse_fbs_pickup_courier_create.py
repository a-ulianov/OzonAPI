from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseFBSPickUpCourierCreateRequest,
    WarehouseFBSPickUpCourierCreateResponse,
)


class WarehouseFBSPickUpCourierCreateMixin(APIManager):
    """Реализует метод /v1/warehouse/fbs/pickup/courier/create"""

    async def warehouse_fbs_pickup_courier_create(
            self: "WarehouseFBSPickUpCourierCreateMixin",
            request: WarehouseFBSPickUpCourierCreateRequest
    ) -> WarehouseFBSPickUpCourierCreateResponse:
        """Создаёт вызов курьера на забор отгрузки pick-up.

        Notes:
            • Тело ответа отсутствует — успешный вызов подтверждается кодом 200.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseFbsPickUpCourierCreate

        Args:
            request: Запрос по схеме `WarehouseFBSPickUpCourierCreateRequest`

        Returns:
            Пустой ответ по схеме `WarehouseFBSPickUpCourierCreateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                await api.warehouse_fbs_pickup_courier_create(
                    WarehouseFBSPickUpCourierCreateRequest(warehouse_id=123)
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/fbs/pickup/courier/create",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseFBSPickUpCourierCreateResponse(**response)
