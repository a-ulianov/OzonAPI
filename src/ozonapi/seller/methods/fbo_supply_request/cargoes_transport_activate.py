from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesTransportActivateRequest,
    CargoesTransportActivateResponse,
)


class CargoesTransportActivateMixin(APIManager):
    """Реализует метод /v1/cargoes/transport/activate"""

    async def cargoes_transport_activate(
            self: "CargoesTransportActivateMixin",
            request: CargoesTransportActivateRequest
    ) -> CargoesTransportActivateResponse:
        """Включает или отключает транспортные грузоместа в поставке FBO.

        Notes:
            • Асинхронная операция; статус — через
              `cargoes_transport_activate_status()` по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос включения транспортных грузомест по схеме
                `CargoesTransportActivateRequest`

        Returns:
            Идентификатор операции по схеме `CargoesTransportActivateResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_transport_activate(
                    CargoesTransportActivateRequest(
                        supply_id=123, is_transport=True
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/activate",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesTransportActivateResponse(**response)
