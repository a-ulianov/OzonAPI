from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesTransportCreateStatusRequest,
    CargoesTransportCreateStatusResponse,
)


class CargoesTransportCreateStatusMixin(APIManager):
    """Реализует метод /v1/cargoes/transport/create/status"""

    async def cargoes_transport_create_status(
            self: "CargoesTransportCreateStatusMixin",
            request: CargoesTransportCreateStatusRequest
    ) -> CargoesTransportCreateStatusResponse:
        """Возвращает статус создания транспортных грузомест.

        Notes:
            • Используйте `operation_id`, полученный методом
              `cargoes_transport_create()`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос статуса создания по схеме
                `CargoesTransportCreateStatusRequest`

        Returns:
            Статус создания по схеме `CargoesTransportCreateStatusResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_transport_create_status(
                    CargoesTransportCreateStatusRequest(operation_id="op-1")
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/create/status",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesTransportCreateStatusResponse(**response)
