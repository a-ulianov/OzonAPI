from ...core import APIManager
from ...schemas.fbo import SupplyOrderPassCreateRequest, SupplyOrderPassCreateResponse


class SupplyOrderPassCreateMixin(APIManager):
    """Реализует метод /v1/supply-order/pass/create"""

    async def supply_order_pass_create(
            self: "SupplyOrderPassCreateMixin",
            request: SupplyOrderPassCreateRequest
    ) -> SupplyOrderPassCreateResponse:
        """Метод для указания данных о водителе и автомобиле для заявки на поставку.

        Notes:
            • Операция асинхронная: метод возвращает `operation_id`, статус выполнения
              проверяйте методом `supply_order_pass_status`.

        References:
            https://docs.ozon.com/api/seller/?#operation/SupplyOrderAPI_CreateSupplyOrderPass

        Args:
            request: Запрос на указание данных о водителе и автомобиле по схеме `SupplyOrderPassCreateRequest`

        Returns:
            Идентификатор операции по схеме `SupplyOrderPassCreateResponse`

        Example:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.supply_order_pass_create(
                    SupplyOrderPassCreateRequest(
                        supply_order_id=1234567890,
                        vehicle=SupplyOrderVehicleInfo(
                            driver_name="Иванов Иван",
                            driver_phone="+79991234567",
                            vehicle_model="ГАЗель",
                            vehicle_number="А123БВ777",
                        ),
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="supply-order/pass/create",
            payload=request.model_dump(by_alias=True)
        )
        return SupplyOrderPassCreateResponse(**response)
