from ...core import APIManager
from ...schemas.fbo_supply_request import (
    CargoesTransportBindRequest,
    CargoesTransportBindResponse,
)


class CargoesTransportBindMixin(APIManager):
    """Реализует метод /v1/cargoes/transport/bind"""

    async def cargoes_transport_bind(
            self: "CargoesTransportBindMixin",
            request: CargoesTransportBindRequest
    ) -> CargoesTransportBindResponse:
        """Связывает или отвязывает грузоместа и транспортные грузоместа.

        Notes:
            • Асинхронная операция; статус — через
              `cargoes_transport_bind_status()` по `operation_id`.

        References:
            https://docs.ozon.ru/api/seller/#tag/FBOTransport

        Args:
            request: Запрос связывания грузомест по схеме
                `CargoesTransportBindRequest`

        Returns:
            Идентификатор операции по схеме `CargoesTransportBindResponse`

        Examples:
            async with SellerAPI(client_id, api_key) as api:
                result = await api.cargoes_transport_bind(
                    CargoesTransportBindRequest(
                        supply_id=123,
                        transport_cargo_bind=[
                            CargoesTransportBindItem(
                                cargo_ids=["1"], transport_cargo_id=10
                            )
                        ],
                    )
                )
        """
        response = await self._request(
            method="post",
            api_version="v1",
            endpoint="cargoes/transport/bind",
            payload=request.model_dump(by_alias=True)
        )
        return CargoesTransportBindResponse(**response)
