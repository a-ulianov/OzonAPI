from ...core import APIManager
from ...schemas.fbp import FbpWarehouseListResponse


class FbpWarehouseListMixin(APIManager):
    """Реализует метод /v1/fbp/warehouse/list"""

    async def fbp_warehouse_list(
            self: "FbpWarehouseListMixin",
    ) -> FbpWarehouseListResponse:
        """Метод для получения списка партнёрских складов FBP.

        Notes:
            • Метод не требует передачи параметров в теле запроса.
            • Возвращает партнёрские склады с адресом, часовым поясом и доступными
              типами поставок.

        References:
            https://docs.ozon.ru/api/seller/?#operation/DeliveryFBPDraft_FbpWarehouseList

        Returns:
            Список партнёрских складов по схеме `FbpWarehouseListResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.fbp_warehouse_list()

            for warehouse in result.warehouses:
                print(warehouse.id, warehouse.name, warehouse.partner_name)
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="fbp/warehouse/list",
            payload={},
        )
        return FbpWarehouseListResponse(**response)
