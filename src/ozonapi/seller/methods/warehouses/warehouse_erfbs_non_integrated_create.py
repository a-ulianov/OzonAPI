from ...core import APIManager
from ...schemas.warehouses import (
    WarehouseERFBSNonIntegratedCreateRequest,
    WarehouseERFBSOperationResponse,
)


class WarehouseERFBSNonIntegratedCreateMixin(APIManager):
    """Реализует метод /v1/warehouse/erfbs/non-integrated/create"""

    async def warehouse_erfbs_non_integrated_create(
            self: "WarehouseERFBSNonIntegratedCreateMixin",
            request: WarehouseERFBSNonIntegratedCreateRequest
    ) -> WarehouseERFBSOperationResponse:
        """Создаёт склад rFBS Express с доставкой «Вы или сторонняя служба».

        Notes:
            • Асинхронная операция; статус — через `warehouse_operation_status()`
              по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#operation/WarehouseERFBSNonIntegratedCreate

        Args:
            request: Запрос по схеме `WarehouseERFBSNonIntegratedCreateRequest`

        Returns:
            Идентификатор операции по схеме `WarehouseERFBSOperationResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.warehouse_erfbs_non_integrated_create(
                    WarehouseERFBSNonIntegratedCreateRequest(name="Склад", phone="+70000000000")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="warehouse/erfbs/non-integrated/create",
            payload=request.model_dump(by_alias=True)
        )
        return WarehouseERFBSOperationResponse(**response)
