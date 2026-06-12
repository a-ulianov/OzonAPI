from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesLabelTransportByOrderStatusRequest,
    CargoesLabelTransportByOrderStatusResponse,
)


class CargoesLabelTransportByOrderStatusMixin(APIManager):
    """Реализует метод /v1/cargoes/label/transport-by-order/status"""

    async def cargoes_label_transport_by_order_status(
            self: "CargoesLabelTransportByOrderStatusMixin",
            request: CargoesLabelTransportByOrderStatusRequest
    ) -> CargoesLabelTransportByOrderStatusResponse:
        """Возвращает статус генерации этикеток транспортных грузомест по поставке.

        Notes:
            • Используйте `operation_id`, полученный методом
              `cargoes_label_transport_by_order_create()`. В `result.file_url` —
              ссылка на файл, в `result.skipped_supplies_ids` — пропущенные
              поставки.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос статуса генерации по схеме
                `CargoesLabelTransportByOrderStatusRequest`

        Returns:
            Статус и ссылку на файл по схеме
            `CargoesLabelTransportByOrderStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_label_transport_by_order_status(
                    CargoesLabelTransportByOrderStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/label/transport-by-order/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesLabelTransportByOrderStatusResponse(**response)
