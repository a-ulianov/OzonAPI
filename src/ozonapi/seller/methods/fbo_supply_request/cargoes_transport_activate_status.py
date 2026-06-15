from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesTransportActivateStatusRequest,
    CargoesTransportActivateStatusResponse,
)


class CargoesTransportActivateStatusMixin(APIManager):
    """Реализует метод /v1/cargoes/transport/activate/status"""

    async def cargoes_transport_activate_status(
            self: "CargoesTransportActivateStatusMixin",
            request: CargoesTransportActivateStatusRequest
    ) -> CargoesTransportActivateStatusResponse:
        """Возвращает статус включения или отключения транспортных грузомест.

        Notes:
            • Используйте `operation_id`, полученный методом
              `cargoes_transport_activate()`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос статуса включения по схеме
                `CargoesTransportActivateStatusRequest`

        Returns:
            Статус операции по схеме `CargoesTransportActivateStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_transport_activate_status(
                    CargoesTransportActivateStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/activate/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesTransportActivateStatusResponse(**response)
