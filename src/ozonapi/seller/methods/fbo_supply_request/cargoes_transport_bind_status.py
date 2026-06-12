from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesTransportBindStatusRequest,
    CargoesTransportBindStatusResponse,
)


class CargoesTransportBindStatusMixin(APIManager):
    """Реализует метод /v1/cargoes/transport/bind/status"""

    async def cargoes_transport_bind_status(
            self: "CargoesTransportBindStatusMixin",
            request: CargoesTransportBindStatusRequest
    ) -> CargoesTransportBindStatusResponse:
        """Возвращает статус связывания или отвязывания грузомест.

        Notes:
            • Используйте `operation_id`, полученный методом
              `cargoes_transport_bind()`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос статуса связывания по схеме
                `CargoesTransportBindStatusRequest`

        Returns:
            Статус операции по схеме `CargoesTransportBindStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_transport_bind_status(
                    CargoesTransportBindStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/bind/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesTransportBindStatusResponse(**response)
